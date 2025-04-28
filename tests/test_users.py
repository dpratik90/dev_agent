=== FILE: tests/test_models.py ===
import pytest
from pydantic import ValidationError
from module import UserBase, UserCreate, User, BaseModel

def test_user_base_model():
    # Test successful creation
    user_base = UserBase(username="test")
    assert user_base.username == "test"
    
    # Test validation error on empty username
    with pytest.raises(ValidationError):
        user_base = UserBase(username="")

def test_user_create_model():
    # Test successful creation
    user_create = UserCreate(username="test", password="password")
    assert user_create.username == "test"
    assert user_create.password == "password"
    
    # Test validation error on empty username
    with pytest.raises(ValidationError):
        user_create = UserCreate(username="", password="password")
        
    # Test validation error on empty password
    with pytest.raises(ValidationError):
        user_create = UserCreate(username="test", password="")

def test_user_model():
    # Test successful creation
    user = User(id=1, username="test", is_active=True)
    assert user.id == 1
    assert user.username == "test"
    assert user.is_active == True
    
    # Test validation error on empty username
    with pytest.raises(ValidationError):
        user = User(id=1, username="", is_active=True)
  
    # Test validation error on empty id
    with pytest.raises(ValidationError):
        user = User(id=None, username="test", is_active=True)

    # Test validation error on empty is_active status
    with pytest.raises(ValidationError):
        user = User(id=1, username="test", is_active=None)