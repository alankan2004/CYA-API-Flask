"""Modified CardModel column names

Revision ID: 7f6ec613dd15
Revises: 39c798e1d447
Create Date: 2020-07-08 11:46:03.909809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f6ec613dd15'
down_revision = '39c798e1d447'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cards', sa.Column('last_review', sa.Date(), nullable=True))
    op.add_column('cards', sa.Column('next_review', sa.Date(), nullable=True))
    op.drop_column('cards', 'last_checked')
    op.drop_column('cards', 'next_check')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cards', sa.Column('next_check', sa.DATE(), nullable=True))
    op.add_column('cards', sa.Column('last_checked', sa.DATE(), nullable=True))
    op.drop_column('cards', 'next_review')
    op.drop_column('cards', 'last_review')
    # ### end Alembic commands ###