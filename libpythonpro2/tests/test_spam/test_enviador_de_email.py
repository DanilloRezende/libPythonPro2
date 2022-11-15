import pytest as pytest

from libpythonpro2.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['renzo@python.pro.br', 'foo@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'luciano@python.pro.br',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
        )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foobar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'luciano@python.pro.br',
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta.'
        )
