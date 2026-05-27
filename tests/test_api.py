def test_listar_produtos(client):

    response=client.get("/api/produtos")

    assert response.status_code==200

    dados=response.json()

    assert len(dados)>0

    assert "nome" in dados[0]
    assert "preco" in dados[0]
    assert "estoque" in dados[0]


def test_compra_sucesso(client):

    response=client.post(
        "/api/comprar",
        json={
            "produto":"teclado",
            "cartao":"123"
        }
    )

    assert response.status_code==200

    assert response.json()["status"]=="sucesso"


def test_produto_inexistente(client):

    response=client.post(
        "/api/comprar",
        json={
            "produto":"ps5",
            "cartao":"123"
        }
    )

    assert response.status_code==404

def test_sem_estoque(client):

    for i in range(10):

        client.post(
            "/api/comprar",
            json={
                "produto":"teclado",
                "cartao":"123"
            }
        )

    response=client.post(
        "/api/comprar",
        json={
            "produto":"teclado",
            "cartao":"123"
        }
    )

    assert response.status_code==400

    assert response.json()["detail"]=="Sem estoque"