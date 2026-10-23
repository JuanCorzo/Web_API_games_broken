# ArcadeShelf API — Parcial de diagnóstico

API de biblioteca de videojuegos construida con FastAPI, SQLModel y SQLite.

El proyecto **arranca correctamente**, pero contiene algunos errores lógicos y de arquitectura que debes diagnosticar y corregir.

## Ejecutar

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
# .\venv\Scripts\Activate.ps1  # Windows PowerShell

python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## Estructura

```text
main.py
database/
models/
schemas/
services/
routers/
```

No cambies esta arquitectura por una lista en memoria ni concentres todo en `main.py`.

Lee `PARCIAL.md` antes de comenzar.
