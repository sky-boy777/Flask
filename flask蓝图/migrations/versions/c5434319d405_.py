"""empty message

Revision ID: c5434319d405
Revises: f02409a0d9db
Create Date: 2020-09-11 23:31:30.502010

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c5434319d405'
down_revision = 'f02409a0d9db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'is_delete',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'is_delete',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###
