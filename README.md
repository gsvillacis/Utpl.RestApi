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
**Ejecute el siguiente comando para inicar la aplicacion**
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

## Modelos
### El proyecto incluye un modelo para la gestión de Incidentes con los siguientes campos: 

Incidente
id: int (opcional)
Fecha_Ingreso: date
Registrado_Por: str
Número_Contacto: str
Descripción_Error: str
Estado: str (por defecto "Nuevo")
Prioridad: str (por defecto "P4")
Resolución: str (opcional)

## Endpoints

- Página de bienvenida: GET / - Devuelve un mensaje de bienvenida.
- Crear un Incidente: POST /Incidentes - Crea un nuevo incidente.
- Consultar Lista de Incidentes: GET /Incidentes - Devuelve una lista de todos los incidentes.
- Actualizar Estado de Incidente: PUT /Incidentes/{incidente_id} - Actualiza el estado de un incidente existente por su ID.
- Eliminar Incidente: DELETE /Incidentes/{incidente_id} - Elimina un incidente por su ID.
- Buscar Incidente por el número de ID: GET /Incidentes/buscar - Busca incidentes por su ID.

## Archivos y Carpetas Principales

- .devcontainer: Ajustes para trabajar con PostgreSQL y Python.
- .github: Configuraciones para la aplicación.
- README.md: Archivo de documentación del proyecto.
- c4model.txt: Codigo de arquitectura de software para la gestion de incidentes. 
- Requirements.txt: Archivo de requisitos para trabajar con PostgreSQL y Python.
