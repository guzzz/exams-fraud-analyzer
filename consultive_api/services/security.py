import jwt

from passlib.hash import django_pbkdf2_sha256


class SecurityService:

    def __init__(self, secret_key) -> None:
        self.__secret_key__ = secret_key
        self.__algorithm__ = "HS256"

    def encode_user(self, username):
        encoded_data = jwt.encode(
            payload={"user": username},
            key=self.__secret_key__,
            algorithm=self.__algorithm__
        )
        return encoded_data

    def decode_token(self, token):
        return jwt.decode(jwt=token, key=self.__secret_key__, algorithms=[self.__algorithm__])

    def check_pwd(self, password, hashed_password):
        return django_pbkdf2_sha256.verify(password, hashed_password)
