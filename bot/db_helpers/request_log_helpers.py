from ..model import Request
from .db_helpers import get_session


def log_request(chat_id, command, params):

    request = Request(chat_id, command, params)
    with get_session() as session:
        session.add(request)
        session.commit()
