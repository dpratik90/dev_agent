=== FILE: tests/test_main.py ===
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..main import get_user, app
from .. import models, schemas

engine = create_engine("sqlite:///./test.db", echo = True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def test_db_session():
    db = TestingSessionLocal()
    yield db
    db.close()

def test_get_user(test_db_session):
    user1 = schemas.UserBase(username="user1", email="user1@example.com", password="password1")
    db_user1 = models.User(**user1.dict())
    test_db_session.add(db_user1)
    test_db_session.commit()
    db_user = get_user(test_db_session, db_user1.id)
    assert db_user.id == db_user1.id

def test_get_user_no_user(test_db_session):
    no_user = get_user(test_db_session, 999)
    assert no_user is None

def test_get_user_non_int_id(test_db_session):
    with pytest.raises(TypeError):
        get_user(test_db_session, "non_int")