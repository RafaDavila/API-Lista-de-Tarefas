from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import tasks

app = FastAPI(
    title="API de Lista de Tarefas",
    description="Primeiro projeto de portfólio",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://localhost:4173",
    "https://todo-app-frontend-e35w.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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