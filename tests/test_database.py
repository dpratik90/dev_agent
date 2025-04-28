import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from sqlalchemy.exc import OperationalError

from module_to_test import Base, SessionLocal

@pytest.fixture(scope="module")
def test_engine():
    return create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)

@pytest.fixture(scope="module")
def test_session_local(test_engine):
    Base.metadata.create_all(bind=test_engine)
    new_session = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    yield new_session
    Base.metadata.drop_all(bind=test_engine)

def test_session_creation(test_session_local):
    session = test_session_local()
    assert session

def test_session_autocommit(test_session_local):
    session = test_session_local()
    assert not session.autocommit

def test_session_autoflush(test_session_local):
    session = test_session_local()
    assert not session.autoflush

def test_engine_creation(test_engine):
    assert test_engine

@pytest.mark.parametrize(
    "database_url", [
        "postgresql://user:password@localhost/db", 
        "sqlite:///:memory:", 
        ""
    ]
)
def test_engine_creation_parameters(database_url):
    if database_url:
        engine = create_engine(database_url, connect_args={"check_same_thread": False}, poolclass=StaticPool)
        assert engine
    else:
        with pytest.raises(OperationalError):
            engine = create_engine(database_url, connect_args={"check_same_thread": False}, poolclass=StaticPool)