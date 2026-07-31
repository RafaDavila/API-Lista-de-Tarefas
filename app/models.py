from sqlalchemy import Boolean, Column, Integer, String, func, DateTime

from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    concluida = Column(Boolean, default=False)
    data_criacao = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )