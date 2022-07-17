from sqlalchemy import Boolean, Column, Integer, MetaData, String, Table
from sqlalchemy.orm import registry

from condominium import domain

mapper_registry = registry()

metadata = MetaData()


unities = Table(
    "unities",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("reference", String(255)),  # check if choices with enum
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("water", Boolean, unique=False, default=True),
    Column("energy", Boolean, unique=False, default=False),
    Column("fire_energy", Boolean, unique=False, default=True),
    Column("internet", Boolean, unique=False, default=False),
    Column("cleaner", Boolean, unique=False, default=True),
    Column("apartments_utilitaries", Boolean, unique=False, default=False),
    Column("generic_utilitaries", Boolean, unique=False, default=True),
)


mapper_registry.map_imperatively(domain.Unity, unities)
