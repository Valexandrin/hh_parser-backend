"""description added

Revision ID: 36a39dbabb71
Revises: b1f0b5353319
Create Date: 2022-06-28 13:05:50.008550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36a39dbabb71'
down_revision = 'b1f0b5353319'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vacancies', sa.Column('description', sa.String(), nullable=True))
    op.alter_column('vacancies', 'status',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vacancies', 'status',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('vacancies', 'description')
    # ### end Alembic commands ###