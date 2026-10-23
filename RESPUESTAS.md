# Respuestas del parcial

1. ¿Qué error encontraste en la validación de `stock`?

El campo aceptaba `0` porque el límite inferior era `ge=0`. El requisito pide un entero entre 1 y 50, así que el mínimo correcto es `ge=1`. Con eso, un stock de 0 responde `422`.

2. ¿Qué hacía que un juego pareciera creado pero no quedara persistido?

En `create_game` se hacía `session.add` y `session.refresh`, pero no `session.commit`. La sesión devolvía el objeto (incluso con `id` si había un flush), y al cerrarse la petición SQLAlchemy hacía rollback. El juego no quedaba en SQLite. El orden correcto es `add`, `commit` y luego `refresh`.

3. ¿Qué problema tenía el endpoint que lista juegos?

`GET /games` declaraba `response_model=GameResponse`, es decir un solo objeto, aunque el servicio devuelve varios registros. FastAPI esperaba un objeto y la respuesta debía ser una lista. Se cambió a `response_model=list[GameResponse]`.

4. ¿Cómo solucionaste la consulta de un ID inexistente?

`session.get` devolvía `None` y el endpoint respondía como si el recurso existiera. Ahora, si no hay juego, se lanza `HTTPException` con estado `404` y `detail` igual a `"Game not found"`.

5. ¿Por qué DELETE podía responder correctamente y aun así no eliminar el registro de SQLite?

`session.delete` solo marca el objeto para borrar dentro de la sesión. Sin `session.commit`, al terminar la petición la transacción se revierte y la fila sigue en la base de datos. Se agregó `session.commit()` después del `delete`.
