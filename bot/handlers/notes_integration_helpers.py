import requests
import posixpath

from ..config import settings


def get_notes_url(note_id=None):
    url = posixpath.join(
        settings.API_NOTES_URL,
        settings.API_NOTES_HANDLER
    )
    if note_id:
        url = posixpath.join(url, note_id)

    return url


def get_notes_by_chat_id(chat_id):

    notes_url = get_notes_url()

    response = requests.get(
        url=notes_url,
        params={'outer_user_id': chat_id},
        auth=(settings.API_NOTES_USER, settings.API_NOTES_USER_PASS)
    )

    notes = []
    if response.status_code == 200:
        notes = response.json()
    return notes


def delete_note(note_id):
    notes_url = get_notes_url(note_id)

    response = requests.delete(
        url=notes_url,
        auth=(settings.API_NOTES_USER, settings.API_NOTES_USER_PASS)
    )

    return response.status_code == 204
