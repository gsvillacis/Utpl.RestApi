from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import date
from datetime import time

app = FastAPI()


class Incidente(BaseModel):
    id: int
    Fecha_Ingreso: date
    Hora_Registro: time
    Registrado_Por: str
    Número_Contacto: int
    Descripción_Error: str
    Estado: str


class Resolución(BaseModel):
    id: int
    Fecha_resolución: date
    Hora_resolución: time
    Resuelto_Por: str
    Descripción_Resolución: str
    Estado: str


# Lista vacía para almacenar los incidentes creados.
Incidentes = []

# Ruta para la página de inicio que devuelve un mensaje de bienvenida.


@app.get('/')
def bienvenida():
    return {'mensaje': 'Welcome a mi aplicación FastAPI Gestión de Incidentes Utpl 2024'}

# Ruta para obtener todos los Incidentes almacenados en la lista.
# El parámetro "response_model" especifica que la respuesta será una lista de objetos "Incidente".


@app.get("/Incidentes", response_model=List[Incidente])
async def consultar_Incidentes():
    return Incidentes

# Ruta para crear un nuevo Incidente.
# El parámetro "response_model" especifica que la respuesta será un objeto "Incidente".
# ES


@app.post("/Incidentes", response_model=Incidente)
async def crear_Incidente(Incidente: Incidente):
    Incidentes.append(Incidente)  # Agrega el incidente a la lista.

    return Incidente

# Ruta para actualizar un Incidente existente por su ID.
# El parámetro "response_model" especifica que la respuesta será un objeto "Incidente".


@app.put("/Incidentes/{Incidente_id}", response_model=Incidente)
async def actualizar_Incidente(Incidente_id: int, Incidente: Incidente):
    Incidentes[Incidente_id] = Incidente  # Actualiza el incidente en la lista.
    return Incidente

# Ruta para eliminar un Incidente por su ID.
# No se especifica "response_model" ya que no se devuelve ningún objeto en la respuesta.
# Este metodo elimina un incidente por su ID.


@app.delete("/Incidentes/{Incidente_id}")
async def eliminar_incidente(Incidente_id: int):
    del Incidentes[Incidente_id]  # Elimina el Incidente de la lista.
    # Devuelve un mensaje informativo.
    return {"mensaje": "Incidente eliminada"}

# Ruta para resolver un Incidente por su ID.
# El parámetro "response_model" especifica que la respuesta será un objeto "incidente".


@app.put("/Incidentes/{Incidente_id}", response_model=Incidente)
async def resolver_Incidente(Incidente_id: int, Incidente: Incidente):
    Incidentes[Incidente_id] = Incidente  # Resuleve el incidente.
    return Incidente
