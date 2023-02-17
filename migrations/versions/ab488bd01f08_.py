"""empty message

Revision ID: ab488bd01f08
Revises: 
Create Date: 2023-02-17 08:38:38.037459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab488bd01f08'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('doors', sa.Integer(), nullable=True),
    sa.Column('engine', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars_model')
    # ### end Alembic commands ###