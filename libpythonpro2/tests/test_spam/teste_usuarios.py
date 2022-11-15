from libpythonpro2.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Renzo', email="renzo@python.pro.br")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)

def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome="Renzo", email="renzo@python.pro.br"),
        Usuario(nome="Luciano", email="Luciano@python.pro.br")
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
