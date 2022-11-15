from unittest.mock import Mock

import pytest

from libpythonpro2 import github_api

@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/81938166?v=4'
    resp_mock.json.return_value = {
        "login": "DanilloRezende",
        "id": 81938166,
        "avatar_url": url
    }
    get_origianl = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_origianl

def test_buscar_avatar(avatar_url):
    url=github_api.buscar_avatar('DanilloRezende')
    assert avatar_url == url

def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('DanilloRezende')
    assert 'https://avatars.githubusercontent.com/u/81938166?v=4' == url