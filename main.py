from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.database import create_db_and_tables
from routers.games import router as games_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="ArcadeShelf API",
    description="API para administrar una pequeña biblioteca de videojuegos.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(games_router)
