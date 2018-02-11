import requests
import posixpath

from ..config import settings


def get_auth_tuple():
    return settings.API_NOTES_USER, settings.API_NOTES_USER_PASS


def get_notes_url(note_id=None):
    url = posixpath.join(
        settings.API_NOTES_URL,
        settings.API_NOTES_HANDLER,
        note_id or ''
    )

    return url


def get_notes_by_chat_id(chat_id):

    notes_url = get_notes_url()

    response = requests.get(
        url=notes_url,
        params={'outer_user_id': chat_id},
        auth=get_auth_tuple()
    )

    notes = []
    if response.status_code == 200:
        notes = response.json()
    return notes


def delete_note(note_id):
    notes_url = get_notes_url(note_id)

    response = requests.delete(
        url=notes_url,
        auth=get_auth_tuple()
    )

    return response.status_code == 204


def get_note_text(note_id):
    notes_url = get_notes_url(note_id)

    response = requests.get(
        url=notes_url,
        auth=get_auth_tuple()
    )

    message = 'Не удалось получить заметку. Попробуйте позднее'
    if response.status_code == 200:
        message = response.json()['text']
    return message


def create_note(chat_id, note_title, note_text):
    notes_url = get_notes_url()

    data = {
        'title': note_title,
        'text': note_text,
        'outer_user_id': chat_id
    }

    response = requests.post(
        url=notes_url,
        data=data,
        auth=get_auth_tuple()
    )

    return response.status_code == 201
