import pytest
from pydantic import ValidationError
from main import UserBase, UserCreate, User

def test_userbase_model():
    # test happy path
    user = UserBase(username='smith')
    assert user.username == 'smith'
    # test missing username
    with pytest.raises(ValidationError):
        user = UserBase()

def test_usercreate_model():
    # test happy path
    user = UserCreate(username='smith', password='secret')
    assert user.username == 'smith'
    assert user.password == 'secret'
    # test missing username
    with pytest.raises(ValidationError):
        user = UserCreate(password='secret')
    # test missing password
    with pytest.raises(ValidationError):
        user = UserCreate(username='smith')

def test_user_model():
    # test happy path
    user = User(id=1, username='smith', is_active=True)
    assert user.id == 1
    assert user.username == 'smith'
    assert user.is_active == True
    # test missing id
    with pytest.raises(ValidationError):
        user = User(username='smith', is_active=True)
    # test missing username
    with pytest.raises(ValidationError):
        user = User(id=1, is_active=True)
    # test missing is_active
    with pytest.raises(ValidationError):
        user = User(id=1, username='smith')