import pytest
from sqlalchemy.orm import Session
from .. import models, schemas

def test_get_user(db: Session):
    # Setup
    user_id = 1
    user = models.User(id=user_id, name="Test User")

    db.add(user)
    db.commit()
    db.refresh(user)

    # Test the function
    result = get_user(db, user_id)

    assert result.id == user_id
    assert result.name == "Test User"

def test_get_user_no_user(db: Session):
    # Setup
    user_id = 2

    # Test the function with a non existent user
    result = get_user(db, user_id)

    assert result is None

def test_get_user_invalid_id(db: Session):
    # Setup
    invalid_id = "Invalid"

    # Test the function with an invalid id
    with pytest.raises(TypeError):
        get_user(db, invalid_id)