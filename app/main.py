from fastapi import FastAPI, Depends, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time

from app.models import Incidente
from sqlmodel import Session, select
from app.db import init_db, get_session

app = FastAPI()


class IncidenteCreate(BaseModel):
    Fecha_Ingreso: date
    Registrado_Por: str
    Número_Contacto: str
    Descripción_Error: str
    Estado: str = "Nuevo"
    Prioridad: str = "P4"
    Resolución: str


class IncidenteU(BaseModel):
    Estado: str = "Nuevo"

# Inicializa la base de datos al iniciar la aplicación.


@app.on_event("startup")
async def on_startup():
    init_db()


@app.get('/')
def bienvenida():
    return {'mensaje': 'Welcome a mi aplicación FastAPI Gestión de Incidentes Utpl 2024-onrender'}


@app.get("/Incidentes", response_model=List[Incidente])
async def consultar_Incidentes(session: Session = Depends(get_session)):
    resultIncidentes = session.exec(select(Incidente)).all()
    return resultIncidentes


@app.post("/Incidentes")
async def crear_Incidente(incidente: IncidenteCreate, session: Session = Depends(get_session)):
    nuevo_incidente = Incidente(
        Fecha_Ingreso=incidente.Fecha_Ingreso,
        Registrado_Por=incidente.Registrado_Por,
        Número_Contacto=incidente.Número_Contacto,
        Descripción_Error=incidente.Descripción_Error,
        Estado=incidente.Estado,
        Prioridad=incidente.Prioridad,
        Resolución=incidente.Resolución
    )
    session.add(nuevo_incidente)
    session.commit()
    session.refresh(nuevo_incidente)
    return nuevo_incidente


@app.put("/Incidentes/{incidente_id}")
async def actualizar_incidente(incidente_id: int, incidenteU: IncidenteU, session: Session = Depends(get_session)):
    existing_incidente = session.get(Incidente, incidente_id)
    if not existing_incidente:
        raise HTTPException(status_code=404, detail="Incidente no encontrado")
    existing_incidente.Estado = incidenteU.Estado
    session.commit()
    return existing_incidente


@app.delete("/Incidentes/{incidente_id}")
async def eliminar_incidente(incidente_id: int, session: Session = Depends(get_session)):
    incidente = session.get(Incidente, incidente_id)
    if not incidente:
        raise HTTPException(status_code=404, detail="Incidente no encontrado")
    session.delete(incidente)
    session.commit()
    return {"mensaje": "Incidente eliminado"}


@app.get("/Incidentes/buscar", response_model=List[Incidente])
async def buscar_Incidentes(descripcion: str, session: Session = Depends(get_session)):
    statement = select(Incidente).where(
        Incidente.Descripción_Error.ilike(f"%{descripcion}%"))
    resultados = session.exec(statement).all()
    return resultados
