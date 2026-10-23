# Parcial práctico — ArcadeShelf API

**Duración:** 1 hora  
**Modalidad:** Individual

## Contexto

ArcadeShelf es una pequeña aplicación para registrar videojuegos disponibles en un club gamer. El proyecto fue construido con FastAPI, SQLModel y SQLite.

La aplicación abre correctamente y Swagger funciona, pero algunos comportamientos no cumplen los requisitos.

Tu trabajo es **diagnosticar y reparar** la aplicación sin reescribirla desde cero.

## Recurso `Game`

Cada juego tiene:

| Campo | Regla |
|---|---|
| `id` | entero generado automáticamente |
| `title` | 3 a 80 caracteres |
| `genre` | 3 a 40 caracteres |
| `platform` | 2 a 30 caracteres |
| `stock` | entero entre 1 y 50 |
| `active` | booleano, `true` por defecto |

## Endpoints esperados

```http
POST   /games
GET    /games
GET    /games/{game_id}
DELETE /games/{game_id}
```

## Pruebas que deben funcionar al final

### P01 — Crear juego válido

```http
POST /games
```

```json
{
  "title": "Hollow Knight",
  "genre": "Metroidvania",
  "platform": "PC",
  "stock": 5
}
```

Debe responder `201 Created`, generar un `id` y conservar `active: true`.

### P02 — Validar stock

Este JSON debe ser rechazado con `422`:

```json
{
  "title": "Celeste",
  "genre": "Plataformas",
  "platform": "PC",
  "stock": 0
}
```

### P03 — Listar juegos

```http
GET /games
```

Debe responder `200` con una **lista** de juegos.

### P04 — Consultar juego existente

```http
GET /games/1
```

Si existe, debe responder `200` con el juego correspondiente.

### P05 — Consultar juego inexistente

```http
GET /games/999
```

Debe responder:

```json
{
  "detail": "Game not found"
}
```

con estado `404`.

### P06 — Eliminar juego

```http
DELETE /games/1
```

Si existe, debe responder:

```json
{
  "message": "Game deleted"
}
```

con `200`.

Después, `GET /games/1` debe responder `404`.

### P07 — Persistencia

1. Crea al menos dos juegos.
2. Consulta `GET /games`.
3. Detén Uvicorn con `Ctrl+C`.
4. Inícialo nuevamente.
5. Consulta `GET /games`.

Los juegos que no fueron eliminados deben continuar allí. Los eliminados no deben reaparecer.

## Reglas

- Conserva `routers/`, `schemas/`, `services/`, `models/` y `database/`.
- No reemplaces SQLite por una lista de Python.
- No reescribas toda la aplicación en `main.py`.
- Puedes usar los comentarios `PISTA` del código.
- Usa Swagger para probar cada corrección.

## Entrega

Sube el proyecto corregido a tu repositorio GitHub y crea `RESPUESTAS.md` con respuestas breves:

1. ¿Qué error encontraste en la validación de `stock`?
2. ¿Qué hacía que un juego pareciera creado pero no quedara persistido?
3. ¿Qué problema tenía el endpoint que lista juegos?
4. ¿Cómo solucionaste la consulta de un ID inexistente?
5. ¿Por qué DELETE podía responder correctamente y aun así no eliminar el registro de SQLite?

## Criterios

| Criterio | Valor |
|---|---:|
| Creación y persistencia | 1.0 |
| Validación | 0.8 |
| Listado | 0.8 |
| Manejo de `404` | 0.8 |
| Eliminación persistente | 0.8 |
| Arquitectura y explicación | 0.8 |
| **Total** | **5.0** |
