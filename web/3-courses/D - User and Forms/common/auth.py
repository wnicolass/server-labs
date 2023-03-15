all = (
    'set_auth_cookie',
    'hash_password'
)

from fastapi import Response, Request
from hashlib import sha512

AUTH_COOKIE_NAME = 'user_id'
SESSION_COOKIE_MAX_AGE = 84600_00
SECRET_KEY = 'adghsah231h4i12351ciubiu1riuu12i1'

def set_auth_cookie(response: Response, user_id: int):
    cookie_value = f'{str(user_id)}:{hash_cookie_value(str(user_id))}'
    response.set_cookie(
        AUTH_COOKIE_NAME,
        cookie_value,
        secure = False,
        httponly = True,
        samesite = 'lax',
        max_age = SESSION_COOKIE_MAX_AGE,
    )
#:

def delete_auth_cookie(response: Response):
    response.delete_cookie(AUTH_COOKIE_NAME)

def hash_cookie_value(cookie_value: str) -> str:
    return sha512(f'{cookie_value}{SECRET_KEY}'.encode('utf-8')).hexdigest()
#:

def hash_password(password: str) -> str:
    return password + '-hashpw'
#:

def get_auth_from_cookie(request: Request) -> int | None:
    if not (cookie_value := request.cookies.get(AUTH_COOKIE_NAME)):
        return None
    
    parts = cookie_value.split(':')
    if len(parts) != 2:
        return None
    
    user_id, hash_value = parts
    hash_check_value = hash_cookie_value(user_id)
    if hash_value != hash_check_value:
        print("Warning: hash mismatch. Invalid cookie value!")
        return None

    return int(user_id) if user_id.isdigit() else None