from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from contextlib import asynccontextmanager

from database import SessionLocal, engine
from models import Base, Conta
from schemas import ContaCreate, Operacao, Transferencia


# 🔹 cria tabelas ao iniciar
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 dependência do banco
async def get_db():
    async with SessionLocal() as session:
        yield session

# 🔹 rota raiz
@app.get("/")
async def raiz():
    return {"msg": "API bancária rodando"}

# 🔹 criar conta
@app.post("/conta")
async def criar_conta(conta: ContaCreate, db: AsyncSession = Depends(get_db)):
    nova_conta = Conta(id=conta.id, saldo=conta.saldo)
    db.add(nova_conta)
    await db.commit()
    return {"msg": "Conta criada com sucesso"}

# 🔹 ver saldo
@app.get("/conta/{conta_id}")
async def ver_saldo(conta_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Conta).where(Conta.id == conta_id))
    conta = result.scalar_one_or_none()

    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    return {"id": conta.id, "saldo": conta.saldo}

# 🔹 depósito
@app.post("/conta/{conta_id}/deposito")
async def depositar(conta_id: int, op: Operacao, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Conta).where(Conta.id == conta_id))
    conta = result.scalar_one_or_none()

    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if op.valor <= 0:
        raise HTTPException(status_code=400, detail="Valor inválido")

    conta.saldo += op.valor
    await db.commit()

    return {"msg": "Depósito realizado", "saldo": conta.saldo}

# 🔹 saque
@app.post("/conta/{conta_id}/saque")
async def sacar(conta_id: int, op: Operacao, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Conta).where(Conta.id == conta_id))
    conta = result.scalar_one_or_none()

    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if op.valor <= 0:
        raise HTTPException(status_code=400, detail="Valor inválido")

    if conta.saldo < op.valor:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")

    conta.saldo -= op.valor
    await db.commit()

    return {"msg": "Saque realizado", "saldo": conta.saldo}

# 🔹 transferência
@app.post("/conta/{conta_id}/transferir")
async def transferir(
    conta_id: int,
    dados: Transferencia,
    db: AsyncSession = Depends(get_db)
):
    # origem
    result_origem = await db.execute(select(Conta).where(Conta.id == conta_id))
    origem = result_origem.scalar_one_or_none()

    if not origem:
        raise HTTPException(status_code=404, detail="Conta origem não encontrada")

    # destino
    result_destino = await db.execute(
        select(Conta).where(Conta.id == dados.conta_destino)
    )
    destino = result_destino.scalar_one_or_none()

    if not destino:
        raise HTTPException(status_code=404, detail="Conta destino não encontrada")

    if dados.valor <= 0:
        raise HTTPException(status_code=400, detail="Valor inválido")

    if origem.id == destino.id:
        raise HTTPException(status_code=400, detail="Mesma conta")

    if origem.saldo < dados.valor:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")

    # operação
    origem.saldo -= dados.valor
    destino.saldo += dados.valor

    await db.commit()

    return {
        "msg": "Transferência realizada",
        "origem_saldo": origem.saldo,
        "destino_saldo": destino.saldo
    }