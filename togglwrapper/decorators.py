from .exceptions import AuthError


def return_json(func):
    """ Returns the JSON content of a requests.Response. """
    def inner(*args, **kwargs):
        response = func(*args, **kwargs)
        return response.json()
    return inner


def error_checking(func):
    """ Raises exceptions if the response did not return 200 OK. """
    def inner(*args, **kwargs):
        response = func(*args, **kwargs)
        # Status code of 403 Forbidden means incorrect API token/wrong auth
        if response.status_code == 403:
            raise AuthError('Incorrect API token.')
        # Raise an HTTPError if status code isn't 200
        response.raise_for_status()
        return response
    return inner
