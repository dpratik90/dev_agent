=== FILE: tests/test_module.py ===
import pytest
from sqlalchemy.orm import Session
from .. import models
from ..main import get_user

class TestGetUser:
    def test_get_user(self, mocker):
        mock_session = mocker.Mock(spec=Session)
        mock_user = mocker.Mock(spec=models.User)
        mock_user.id = 1
        mock_query = mocker.Mock()
        mock_filter = mocker.Mock()
        mock_query.filter.return_value = mock_filter
        mock_filter.first.return_value = mock_user
        mock_session.query.return_value = mock_query
        user = get_user(mock_session, 1)
        mock_session.query.assert_called_once_with(models.User)
        mock_filter.assert_called_once_with(models.User.id == 1)
        assert user == mock_user

    def test_get_user_none(self, mocker):
        mock_session = mocker.Mock(spec=Session)
        mock_query = mocker.Mock()
        mock_filter = mocker.Mock()
        mock_query.filter.return_value = mock_filter
        mock_filter.first.return_value = None
        mock_session.query.return_value = mock_query
        user = get_user(mock_session, 1)
        mock_session.query.assert_called_once_with(models.User)
        mock_filter.assert_called_once_with(models.User.id == 1)
        assert user is None

@pytest.fixture
def mocker():
    from unittest import mock
    return mock.Mock()