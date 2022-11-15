from unittest.mock import Mock

import pytest

from libpythonpro2.spam.enviador_de_email import Enviador
from libpythonpro2.spam.main import EnviadorDeSpam
from libpythonpro2.spam.modelos import Usuario

@pytest.mark.parametrize(
    'usuarios',
        [
            [
                Usuario(nome="Renzo", email="renzo@python.pro.br"),
                Usuario(nome="Luciano", email="luciano@python.pro.br")
            ],
            [
                Usuario(nome='Renzo', email="renzo@python.pro.br")
            ]
        ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count

def test_parametros_de_spam(sessao):
    usuario = Usuario(nome="Renzo", email="renzo@python.pro.br")
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        "luciano@python.pro.br",
        'Curso Python Pro',
        'Confira que estudo fantástico'
    )
    enviador.enviar.assert_called_once_with(
        "luciano@python.pro.br",
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira que estudo fantástico'
    )