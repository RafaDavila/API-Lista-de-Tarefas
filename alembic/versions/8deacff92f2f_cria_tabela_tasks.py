"""cria tabela tasks

Revision ID: 8deacff92f2f
Revises: 
Create Date: 2026-07-31 17:06:27.258684

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8deacff92f2f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Cria a tabela inicial de tarefas."""
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("titulo", sa.String(), nullable=False),
        sa.Column("descricao", sa.String(), nullable=True),
        sa.Column(
            "concluida",
            sa.Boolean(),
            server_default=sa.false(),
            nullable=False
        ),
        sa.PrimaryKeyConstraint("id")
    )

    op.create_index(
        op.f("ix_tasks_id"),
        "tasks",
        ["id"],
        unique=False
    )


def downgrade() -> None:
    """Remove a tabela inicial de tarefas."""
    op.drop_index(op.f("ix_tasks_id"), table_name="tasks")
    op.drop_table("tasks")
