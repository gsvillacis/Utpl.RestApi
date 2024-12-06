# Utpl.RestApi
Proyecto para trabajar con Api en REST utilizando fastapi


## Descripción del Proyecto

**Este proyecto es una aplicación web construida utilizando FastAPI.** FastAPI es un framework de Python moderno, rápido y fácil de usar para crear APIs. Es ideal para construir aplicaciones web backend que necesitan ser eficientes y escalables.

## Requisitos

* **Python:** Asegúrate de tener Python 3.6 o superior instalado.
* **FastAPI:** Instala FastAPI usando pip:
  ```bash
  pip install fastapi uvicorn

## Documentación 

## Ejecucion
Ejecute el siguiente comando para inicar la aplicacion
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

##Modelos
Incidente
id: int (opcional)
Fecha_Ingreso: date
Registrado_Por: str
Número_Contacto: str
Descripción_Error: str
Estado: str (por defecto "Nuevo")
Prioridad: str (por defecto "P4")
Resolución: str (opcional)

IncidenteU
Estado: str (por defecto "Nuevo")

## Ejecucion
Página de bienvenida
GET /

Devuelve un mensaje de bienvenida.

Respuesta:

{
    "mensaje": "Welcome a mi aplicación FastAPI Gestión de Incidentes Utpl 2024"
}

Crear Incidente
POST /Incidentes

Crea un nuevo incidente.

Cuerpo de la solicitud:
{
    "Fecha_Ingreso": "2024-01-01",
    "Registrado_Por": "Gissela Villacis",
    "Número_Contacto": "1716829161",
    "Descripción_Error": "Error de prueba"
}

Consultar Incidentes
GET /Incidentes

Devuelve una lista de todos los incidentes.

Respuesta:
[
    {
        "id": 1,
        "Fecha_Ingreso": "2024-01-01",
        "Registrado_Por": "Gissela Villacis",
        "Número_Contacto": "1716829161",
        "Descripción_Error": "Error de prueba",
        "Estado": "Nuevo",
        "Prioridad": "P4",
        "Resolución": null
    }
]


Actualizar Incidente
PUT /Incidentes/{incidente_id}

Actualiza el estado de un incidente existente.

Cuerpo de la solicitud:

{
    "Estado": "En Proceso"
}

respuesta: 
{
    "id": 1,
    "Fecha_Ingreso": "2024-01-01",
    "Registrado_Por": "Juan Perez",
    "Número_Contacto": "1234567890",
    "Descripción_Error": "Error de prueba",
    "Estado": "En Proceso",
    "Prioridad": "P4",
    "Resolución": null
}

Eliminar Incidente
DELETE /Incidentes/{incidente_id}

Elimina un incidente por su ID.

Respuesta:
{
    "mensaje": "Incidente eliminado"
}

Buscar Incidentes
GET /Incidentes/buscar

Busca incidentes por su descripción.

Parámetros de consulta:

descripcion: Descripción del error a buscar.
Respuesta:

[
    {
        "id": 1,
        "Fecha_Ingreso": "2024-01-01",
        "Registrado_Por": "Juan Perez",
        "Número_Contacto": "1234567890",
        "Descripción_Error": "Error de prueba",
        "Estado": "Nuevo",
        "Prioridad": "P4",
        "Resolución": null
    }
]