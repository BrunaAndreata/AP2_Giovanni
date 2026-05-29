from pytest_bdd import scenarios, given, when, then
from pathlib import Path


FEATURES = Path(__file__).parent / "features"

scenarios(str(FEATURES / "comprar_produto.feature"))


@given(
    "que existe um produto disponível",
    target_fixture="produto"
)
def produto():

    return "teclado"


@when(
    "o cliente compra o produto",
    target_fixture="resposta"
)
def comprar(client, produto):

    resposta = client.post(
        "/api/comprar",
        json={
            "produto": produto,
            "cartao": "123456"
        }
    )

    return resposta


@then("a compra deve ser aprovada")
def validar(resposta):

    assert resposta.status_code == 200