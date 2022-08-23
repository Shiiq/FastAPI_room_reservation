"""add reservation model

Revision ID: e5821e25b9cf
Revises: 74ff525c5430
Create Date: 2022-08-23 21:06:17.562260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5821e25b9cf'
down_revision = '74ff525c5430'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_reserve', sa.DateTime(), nullable=True),
    sa.Column('to_reserve', sa.DateTime(), nullable=True),
    sa.Column('meetingroom_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meetingroom_id'], ['meetingroom.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    # ### end Alembic commands ###