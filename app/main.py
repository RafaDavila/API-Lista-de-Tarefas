from fastapi import FastAPI

from app.database import Base, engine
from app.routers import tasks

app = FastAPI(
    title="API de Lista de Tarefas",
    description="Primeiro projeto de portfólio",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(tasks.router)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Bem-vindo à ToDo API",
        "documentation": "/docs",
        "health": "/health"
    }