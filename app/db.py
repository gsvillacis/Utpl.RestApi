import os

from sqlmodel import create_engine, SQLModel, Session


database_url = "postgresql://userincidentes:CW5LAfeBwyzq97xlH9F8ueaKaIsR5jg0@dpg-ctj1d5t2ng1s73bg1in0-a.oregon-postgres.render.com/dbincidentes_gcfp"

# Crear el motor de la base de datos
engine = create_engine(database_url, echo=True)

# Función para inicializar la base de datos


def init_db():
    SQLModel.metadata.create_all(engine)

# Función para obtener la sesión de la base de datos
    def get_session():
        with Session(engine) as session:
            yield session
