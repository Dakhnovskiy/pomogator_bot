from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..config import settings

__engine = create_engine(settings.DATABASE)
__session_maker = sessionmaker(bind=__engine)


def get_engine():
    return __engine


@contextmanager
def get_session():
    session = __session_maker()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
