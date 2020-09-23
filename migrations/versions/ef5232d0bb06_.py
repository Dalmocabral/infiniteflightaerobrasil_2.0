"""empty message

Revision ID: ef5232d0bb06
Revises: 
Create Date: 2020-07-25 18:02:12.210398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef5232d0bb06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('sobrenome', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('gametag', sa.String(length=200), nullable=True),
    sa.Column('registro', sa.String(length=200), nullable=True),
    sa.Column('ifcomunity', sa.String(length=400), nullable=True),
    sa.Column('sobremim', sa.String(length=200), nullable=True),
    sa.Column('pais', sa.String(length=200), nullable=True),
    sa.Column('base', sa.String(length=200), nullable=True),
    sa.Column('idade', sa.String(length=200), nullable=True),
    sa.Column('grau', sa.String(length=200), nullable=True),
    sa.Column('data_create', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('logbooks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('saida', sa.String(length=200), nullable=True),
    sa.Column('chegada', sa.String(length=200), nullable=True),
    sa.Column('aeronave', sa.String(length=200), nullable=True),
    sa.Column('voo', sa.String(length=200), nullable=True),
    sa.Column('tempo', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('data_create', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logbooks')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
