import sqlalchemy as sa

from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class MessageBase(SQLModel):
    client_id: str
    text: str
    created: datetime = Field(
        sa_column=sa.Column(
            sa.DateTime(timezone=True), 
            server_default=sa.func.now()
        )
    )


class Message(MessageBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)

