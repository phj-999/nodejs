"""drop table student address

Revision ID: 95b885705cd6
Revises: 73d980c447c6
Create Date: 2022-10-09 18:11:20.680840

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '95b885705cd6'
down_revision = '73d980c447c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_migrate_student_address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_migrate_student_address',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False, comment='主键'),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True, comment='地址名称'),
    sa.Column('province', mysql.VARCHAR(length=50), nullable=True, comment='省份'),
    sa.Column('city', mysql.VARCHAR(length=50), nullable=True, comment='城市'),
    sa.Column('area', mysql.VARCHAR(length=50), nullable=True, comment='地区'),
    sa.Column('address', mysql.VARCHAR(length=500), nullable=True, comment='详细地址'),
    sa.Column('mobile', mysql.VARCHAR(length=15), nullable=True, comment='收货人电话'),
    sa.Column('student_id', mysql.INTEGER(), autoincrement=False, nullable=True, comment='student外键'),
    sa.ForeignKeyConstraint(['student_id'], ['t_migrate_student.id'], name='t_migrate_student_address_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
