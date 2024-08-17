from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import DBAPIError

from app.core.config import settings

engine = create_engine(url=settings.db_url, echo=False)
sessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    session = sessionMaker()
    try:
        yield session
    except DBAPIError:
        session.rollback()
    finally:
        session.close()
