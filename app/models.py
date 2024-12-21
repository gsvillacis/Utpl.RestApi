from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel
from datetime import date, time


class Incidente(SQLModel, table=True):
    # Hacer que el ID sea opcional para que no sea requerido en la creación.
    id: Optional[int] = Field(default=None, primary_key=True)
    Fecha_Ingreso: date
    Registrado_Por: str
    # Cambiar a str para evitar problemas con números de contacto largos.
    Número_Contacto: str
    Descripción_Error: str
    Estado: str = "Nuevo"
    Prioridad: str = "P4"
    Resolución: Optional[str] = None
