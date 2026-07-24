from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import Base, engine, get_db

app = FastAPI(
    title="API de Lista de Tarefas",
    description="Primeiro projeto de portfólio",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(
    task:schemas.TaskCreate,
    db: Session = Depends(get_db)
):
    return crud.create_task(db, task)

@app.get("/tasks", response_model=list[schemas.TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )
    return task

@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(get_db)
):
    updated_task = crud.update_task(db, task_id, task)
    if updated_task is None:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )
    return updated_task

@app.delete("/tasks/{task_id}", response_model=schemas.TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db, task_id)

    if deleted_task is None:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )
    return deleted_task