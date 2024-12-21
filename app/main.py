from fastapi import FastAPI, Depends, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time

from app.models import Incidente
from sqlmodel import Session, select
from app.db import init_db, get_session

app = FastAPI()


class IncidenteU(BaseModel):
    # Hacer que el ID sea opcional para que no sea requerido en la creación.
    Estado: str = "Nuevo"


# Lista vacía para almacenar los incidentes creados.
Incidentes = []

# Inicializa la base de datos al iniciar la aplicación.


@app.on_event("startup")
def on_startup():
    init_db()

# Ruta para la página de inicio que devuelve un mensaje de bienvenida.


@app.get('/')
def bienvenida():
    return {'mensaje': 'Welcome a mi aplicación FastAPI Gestión de Incidentes Utpl 2024-onrender'}

# Ruta para obtener todos los Incidentes almacenados en la lista.
# El parámetro "response_model" especifica que la respuesta será una lista de objetos "Incidente".


@app.get("/Incidentes", response_model=List[Incidente])
async def consultar_Incidentes(session: Session = Depends(get_session)):
    resultIncidentes = session.exec(select(Incidente)).all()
    return resultIncidentes

# Ruta para crear un nuevo Incidente.
# El parámetro "response_model" especifica que la respuesta será un objeto "Incidente".
# ES


@app.post("/Incidentes", response_model=Incidente)
async def crear_Incidente(incidente: Incidente, session: Session = Depends(get_session)):
    session.add(incidente)  # Agrega el incidente a la lista.
    session.commit()
    session.refresh(incidente)

    return incidente

# Ruta para actualizar un Incidente existente por su ID.
# El parámetro "response_model" especifica que la respuesta será un objeto "Incidente".


@app.put("/Incidentes/{incidente_id}", response_model=Incidente)
async def actualizar_Incidente(incidente_id: int, incidenteU: IncidenteU):
    for idx, existing_incidente in enumerate(Incidentes):
        if existing_incidente.id == incidente_id:
            # Imprime la información registrada
            print(f"Información registrada: {existing_incidente.dict()}")
            existing_incidente.Estado = incidenteU.Estado
            return existing_incidente
    raise HTTPException(status_code=404, detail="Incidente no encontrado")

# Ruta para eliminar un Incidente por su ID.
# No se especifica "response_model" ya que no se devuelve ningún objeto en la respuesta.
# Este metodo elimina un incidente por su ID.


@app.delete("/Incidentes/{incidente_id}")
async def eliminar_incidente(incidente_id: int, session: Session = Depends(get_session)):
    for idx, existing_incidente in enumerate(Incidentes):
        if existing_incidente.id == incidente_id:
            del Incidentes[idx]  # Elimina el incidente de la lista.
            return {"mensaje": "Incidente eliminado"}
    raise HTTPException(status_code=404, detail="Incidente no encontrado")

session.delete(incidente)
session.commit()

return {"mensaje": "Incidente eliminado"}

# Ruta para buscar incidentes por su descripción.


@app.get("/Incidentes/buscar", response_model=List[Incidente])
async def buscar_Incidentes(descripcion: str):
    resultados = [incidente for incidente in Incidentes if descripcion.lower(
    ) in incidente.Descripción_Error.lower()]
    return resultados
