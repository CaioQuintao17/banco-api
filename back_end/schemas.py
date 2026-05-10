from pydantic import BaseModel

class ContaCreate(BaseModel):
    id: int
    saldo: float = 0.0

class Operacao(BaseModel):
    valor: float

class Transferencia(BaseModel):
    conta_destino: int
    valor: float