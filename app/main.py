from fastapi import FastAPI, Depends, HTTPException, Query, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time

from app.Utils.Auth import create_user, get_user
from app.models import GetUser, Incidente, PostUser
from sqlmodel import Session, select
from app.db import init_db, get_session

from app.security import verification

# para trabajar con telegram

from app.Utils.telegram_service import send_message_telegram

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
async def consultar_Incidentes(session: Session = Depends(get_session), verification=Depends(verification)):
    resultIncidentes = session.exec(select(Incidente)).all()
    return resultIncidentes


@app.post("/Incidentes")
async def crear_Incidente(incidente: IncidenteCreate, session: Session = Depends(get_session), verification=Depends(verification)):
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

    # Enviar mensaje a Telegram

    await send_message_telegram(
        f"🚨 Nuevo incidente creado: \n\n"
        f"Numero de ticket: {nuevo_incidente.id}\n"
        f"Error: {nuevo_incidente.Descripción_Error}\n"
        f"Estado: {nuevo_incidente.Estado}\n"
        f"Prioridad: {nuevo_incidente.Prioridad}\n"
        f"Fecha de ingreso: {nuevo_incidente.Fecha_Ingreso}\n"
        f"Registrado por: {nuevo_incidente.Registrado_Por}\n"
        f"Contacto: {nuevo_incidente.Número_Contacto}")

    return nuevo_incidente


@ app.put("/Incidentes/{incidente_id}")
async def actualizar_incidente(incidente_id: int, incidenteU: IncidenteU, session: Session = Depends(get_session), verification=Depends(verification)):
    existing_incidente = session.get(Incidente, incidente_id)
    if not existing_incidente:
        raise HTTPException(status_code=404, detail="Incidente no encontrado")
    existing_incidente.Estado = incidenteU.Estado
    session.commit()
    return existing_incidente


@ app.delete("/Incidentes/{incidente_id}")
async def eliminar_incidente(incidente_id: int, session: Session = Depends(get_session), verification=Depends(verification)):
    incidente = session.get(Incidente, incidente_id)
    if not incidente:
        raise HTTPException(status_code=404, detail="Incidente no encontrado")
    session.delete(incidente)
    session.commit()
    return {"mensaje": "Incidente eliminado"}


@ app.get("/Incidentes/buscar", response_model=List[Incidente])
async def buscar_Incidentes(id: int, session: Session = Depends(get_session), verification=Depends(verification)):
    statement = select(Incidente).where(Incidente.id == id)
    resultados = session.exec(statement).all()
    if not resultados:
        raise HTTPException(status_code=404, detail="Incidente no encontrado")
    return resultados

# registro de usuarios using email, username, password


@ app.post("/register", response_model=GetUser, tags=["usuarios"])
def register_user(payload: PostUser, session: Session = Depends(get_session)):

    if not payload.email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please add Email",
        )
    user = get_user(session, payload.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"User with email {payload.email} already exists",
        )
    user = create_user(session, payload)
    print(user)

    return user
