import pytest
from fastapi import status, HTTPException
from jose import JWTError, jwt
from unittest.mock import MagicMock, patch
from app.crud.get_user import get_user
from main import JWTBearer, oauth2_scheme

def setup_module(module):
    module.VALID_TOKEN = jwt.encode({"sub": "test_user"}, "YOUR-SECRET-KEY")
    module.INVALID_TOKEN = jwt.encode({"not_sub": "test_user"}, "YOUR-SECRET-KEY")

@pytest.fixture
def mock_get_user():
    mock_user = MagicMock(name="user")
    with patch("main.get_user", return_value=mock_user) as mock_get_user:
        yield mock_get_user

def test_JWTBearer_with_valid_token(mock_get_user):
    mock_get_user.authorization_scheme_prefix = "Bearer"
    token_data = JWTBearer(token=VALID_TOKEN)
    assert token_data.username == "test_user"
    assert mock_get_user.call_count

def test_JWTBearer_with_invalid_token(mock_get_user):
    mock_get_user.authorization_scheme_prefix = "Bearer"
    with pytest.raises(HTTPException) as excinfo:
        JWTBearer(token=INVALID_TOKEN)
    
    assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert mock_get_user.call_count

def test_JWTBearer_no_token(mock_get_user):
    mock_get_user.authorization_scheme_prefix = "Bearer"
    with pytest.raises(HTTPException) as excinfo:
        JWTBearer()
    assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert mock_get_user.call_count

def test_JWTBearer_JWTError_raised(mock_get_user):
    mock_get_user.authorization_scheme_prefix = "Bearer"
    with patch("main.jwt.decode", side_effect=JWTError):
        with pytest.raises(HTTPException) as excinfo:
            JWTBearer(token=VALID_TOKEN)
        assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED
        assert mock_get_user.call_count