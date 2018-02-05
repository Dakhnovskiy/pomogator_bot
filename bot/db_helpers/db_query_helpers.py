from .db_helpers import get_session
from ..model import Request


def get_params_from_last_request(chat_id, command):
    session = get_session()

    last_request = session.query(Request).filter(
        Request.chat_id == chat_id, Request.command == command
    ).order_by(Request.date.desc()).first()
    params = {}
    if last_request:
        for param in last_request.params:
            params[param.name] = param.value

    return params
