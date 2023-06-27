"""Initial migration

Revision ID: 549b2d776841
Revises: 
Create Date: 2023-06-22 12:45:35.927857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '549b2d776841'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sales',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sales_type', sa.String(length=1), nullable=True),
    sa.Column('sales_date', sa.String(length=26), nullable=True),
    sa.Column('product_description', sa.String(length=31), nullable=True),
    sa.Column('product_price', sa.String(length=10), nullable=True),
    sa.Column('vendor_name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sales')
    # ### end Alembic commands ###
