"""Increased password constraint size

Revision ID: f6ebe0547fac
Revises: 967a7f8ba8f1
Create Date: 2022-07-14 11:59:49.158833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6ebe0547fac'
down_revision = '967a7f8ba8f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=250),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=100),
               existing_nullable=True)
    # ### end Alembic commands ###