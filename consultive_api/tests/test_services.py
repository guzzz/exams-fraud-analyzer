
import jwt

from passlib.hash import django_pbkdf2_sha256

from consultive_api.services.security import *
from consultive_api.services.security import SecurityService

TEST_SECRET_KEY = 'gi9#t2@+1k&@(gq3dq_s^n-6d-7nahk^14g2-w=t*qk0m#2$(='
security_service = SecurityService(TEST_SECRET_KEY)


def test_encode_user():
    expected_result = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGVhZHBvb2wifQ.sk437_FAoKUpBOuTldQcw-K1fWW9PpA2dQQDpAlSmhQ'
    result = security_service.encode_user("deadpool")
    assert result == expected_result

def test_decode_user():
    expected_result = {'user': 'deadpool'}
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGVhZHBvb2wifQ.sk437_FAoKUpBOuTldQcw-K1fWW9PpA2dQQDpAlSmhQ'
    result = security_service.decode_token(token)
    assert result == expected_result
