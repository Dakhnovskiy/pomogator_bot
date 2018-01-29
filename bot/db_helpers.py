from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings


def get_engine():
    return create_engine(settings.DATABASE)


def get_session():
    engine = get_engine()
    session_maker = sessionmaker(bind=engine)
    return session_maker()
