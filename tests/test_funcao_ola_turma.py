from app.funcao import funcao_ola_turma

def test_funcao_ola_turma_retorna_ola_jornada():
    saida = funcao_ola_turma()
    gabarito = "Olá Jornada"
    assert saida == gabarito