=== FILE: tests/test_models.py ===
import pytest
from pydantic import ValidationError
from models import UserBase, UserCreate, User 

def test_user_base_model():
    user_base = UserBase(username="testuser")
    assert user_base.username == "testuser"

    with pytest.raises(ValidationError):
        user_base = UserBase(username="")


def test_user_create_model():
    user_create = UserCreate(username="testuser", password="password")
    assert user_create.username == "testuser"
    assert user_create.password == "password"

    with pytest.raises(ValidationError):
        user_create = UserCreate(username="testuser", password="")

    with pytest.raises(ValidationError):
        user_create = UserCreate(username="", password="password")


def test_user_model():
    user = User(id=1, username="testuser", is_active=True)
    assert user.id == 1
    assert user.username == "testuser"
    assert user.is_active is True

    with pytest.raises(ValidationError):
        user = User(id="", username="testuser", is_active=True)

    with pytest.raises(ValidationError):
        user = User(id=1, username="", is_active=True)

    with pytest.raises(ValidationError):
        user = User(id=1, username="testuser", is_active="")