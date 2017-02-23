"""empty message

Revision ID: f20fe5b79ac5
Revises: 
Create Date: 2017-02-11 12:56:42.895881

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f20fe5b79ac5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'auto_dealer', 'automotive_business', ['id'], ['id'])
    op.create_foreign_key(None, 'automotive_business', 'local_business', ['id'], ['id'])
    op.alter_column('geocoords', 'latitude',
               existing_type=mysql.VARCHAR(length=1024),
               type_=sa.Float(),
               existing_nullable=True)
    op.alter_column('geocoords', 'longitude',
               existing_type=mysql.VARCHAR(length=1024),
               type_=sa.Float(),
               existing_nullable=True)
    op.create_index('uix_1', 'geocoords', ['latitude', 'longitude'], unique=True)
    op.create_foreign_key(None, 'historic_place', 'place', ['id'], ['guid'])
    op.create_foreign_key(None, 'landmark', 'place', ['id'], ['guid'])
    op.create_foreign_key(None, 'local_business', 'place', ['id'], ['guid'])
    op.create_foreign_key(None, 'org_areas', 'place', ['place_id'], ['guid'])
    op.create_foreign_key(None, 'org_areas', 'organization', ['org_id'], ['guid'])
    op.create_foreign_key(None, 'place', 'geocoords', ['geo_id'], ['guid'])
    op.create_foreign_key(None, 'postaladdress', 'geocoords', ['geo_id'], ['guid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'postaladdress', type_='foreignkey')
    op.drop_constraint(None, 'place', type_='foreignkey')
    op.drop_constraint(None, 'org_areas', type_='foreignkey')
    op.drop_constraint(None, 'org_areas', type_='foreignkey')
    op.drop_constraint(None, 'local_business', type_='foreignkey')
    op.drop_constraint(None, 'landmark', type_='foreignkey')
    op.drop_constraint(None, 'historic_place', type_='foreignkey')
    op.drop_index('uix_1', table_name='geocoords')
    op.alter_column('geocoords', 'longitude',
               existing_type=sa.Float(),
               type_=mysql.VARCHAR(length=1024),
               existing_nullable=True)
    op.alter_column('geocoords', 'latitude',
               existing_type=sa.Float(),
               type_=mysql.VARCHAR(length=1024),
               existing_nullable=True)
    op.drop_constraint(None, 'automotive_business', type_='foreignkey')
    op.drop_constraint(None, 'auto_dealer', type_='foreignkey')
    # ### end Alembic commands ###