from unittest.mock import Mock

from libpythonpro2 import github_api


def test_buscar_avatar():
    resp_mock= Mock()
    resp_mock.json.return_value = {
        "login": "DanilloRezende",
        "id": 81938166,
        "avatar_url": "https://avatars.githubusercontent.com/u/81938166?v=4"
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url=github_api.buscar_avatar('DanilloRezende')
    assert 'https://avatars.githubusercontent.com/u/81938166?v=4' == url