from sqlalchemy.orm import Session

from app import models, schemas


def create_task(db: Session, task: schemas.TaskCreate):
    nova_task = models.Task(
        titulo=task.titulo,
        descricao=task.descricao,
    )

    db.add(nova_task)
    db.commit()
    db.refresh(nova_task)

    return nova_task


def get_tasks(db: Session):
    return db.query(models.Task).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    db_task = get_task(db, task_id)
    if db_task is None:
        return None
    db_task.titulo = task.titulo
    db_task.descricao = task.descricao
    db_task.concluida = task.concluida 

    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if db_task is None:
        return None
    db.delete(db_task)
    db.commit()
    return db_task

