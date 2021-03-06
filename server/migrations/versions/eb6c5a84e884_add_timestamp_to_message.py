"""Add timestamp to message

Revision ID: eb6c5a84e884
Revises: fb85f24f4082
Create Date: 2021-11-30 16:39:06.732049

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'eb6c5a84e884'
down_revision = 'fb85f24f4082'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('message', 'created')
    # ### end Alembic commands ###
