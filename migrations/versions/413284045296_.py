"""empty message

Revision ID: 413284045296
Revises: 
Create Date: 2021-07-30 20:37:35.416521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '413284045296'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('manufacturer', sa.String(length=35), nullable=False),
    sa.Column('price', sa.DECIMAL(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_name'), 'products', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_name'), table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###
