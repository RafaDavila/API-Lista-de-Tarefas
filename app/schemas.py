from pydantic import BaseModel, ConfigDict, Field

class TaskBase(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100, description="Título da tarefa")
    descricao: str | None = Field(
        default = None,
        max_length=500,
        description="Descrição da tarefa"
    )


class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    concluida: bool | None = None

class TaskResponse(TaskBase):
    id: int
    concluida: bool

    model_config = ConfigDict(from_attributes=True)