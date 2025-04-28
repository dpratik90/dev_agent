=== FILE: tests/test_auth.py ===
import pytest
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from auth_module import JWTBearer
from auth_module.crud.get_user import get_user

class TestJWTBearer:
    @pytest.fixture(scope="module")
    def token(self):
        return jwt.encode({"sub": "username"}, "YOUR-SECRET-KEY")

    @pytest.fixture(scope="module")
    def badly_encoded_token(self):
        return "badly encoded jwt token"

    @pytest.fixture(scope="module")
    def empty_username_token(self):
        return jwt.encode({"sub": ""}, "YOUR-SECRET-KEY")

    def test_decode_token(self, token):
        assert JWTBearer(user=get_user("username"), token=token) is not None

    def test_decode_badly_encoded_token(self, badly_encoded_token):
        with pytest.raises(HTTPException) as excinfo:
            JWTBearer(user=get_user("username"), token=badly_encoded_token)
        assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED

    def test_decode_empty_username_token(self, empty_username_token):
        with pytest.raises(HTTPException) as excinfo:
            JWTBearer(user=get_user("username"), token=empty_username_token)
        assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED

=== FILE: conftest.py ===
import pytest
from auth_module.crud.get_user import get_user

@pytest.fixture
def user():
    return get_user("username")