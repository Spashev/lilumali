import contextlib

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app import api, handle_exceptions
from app.core.config import settings
from app.models.budget import Base
from app.database.base import engine
from app import api, handle_exceptions
from app.core.config import settings


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    handle_exceptions(app=app)
    yield


def initialize():
    app = FastAPI(
        title='Budget',
        debug=settings.DEBUG,
        version='0.0.1',
        docs_url='/swagger',
        redoc_url='/redoc',
        lifespan=lifespan,
    )
    app.include_router(api.router)

    return app


app = initialize()
