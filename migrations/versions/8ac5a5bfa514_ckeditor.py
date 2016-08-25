"""ckeditor

Revision ID: 8ac5a5bfa514
Revises: efced864c034
Create Date: 2016-08-25 16:29:38.592091

"""

# revision identifiers, used by Alembic.
revision = '8ac5a5bfa514'
down_revision = 'efced864c034'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('title', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'title')
    ### end Alembic commands ###
