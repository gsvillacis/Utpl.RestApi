import os

from sqlmodel import create_engine, SQLModel, Session

database_url = "postgresql://userincidentes:CW5LAfeBwyzq97xlH9F8ueaKaIsR5jg0@dpg-ctj1d5t2ng1s73bg1in0-a.oregon-postgres.render.com/dbincidentes_gcfp"


def create_db_and_tables():
    engine = create_engine(database_url)
    SQLModel.metadata.create_all(engine)
