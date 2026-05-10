from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()

class Conta(Base):
    __tablename__ = "contas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    saldo: Mapped[float] = mapped_column(default=0.0)