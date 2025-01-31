import os
from sqlmodel import create_engine, SQLModel, Session

database_url = "postgresql://userincidentesbp:BGBAnpvhxPMk3nM0HvfxBRaMT6Tk073i@dpg-cueic1ogph6c73fbjou0-a.oregon-postgres.render.com/dbincidentesbp"

# Conexión a la base de datos
engine = create_engine(database_url, echo=True)

# Función para inicializar la base de datos


def init_db():
    SQLModel.metadata.create_all(engine)

# Función para obtener una sesión de la base de datos


def get_session():
    with Session(engine) as session:
        yield session
