from ..model import Request
from .db_helpers import get_session


def log_request(chat_id, command, params):

    request = Request(chat_id, command, params)
    session = get_session()
    try:
        session.add(request)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
