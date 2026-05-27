from unittest.mock import Mock
from main import processar_pedido
import pytest

def test_gateway_aprovado():

    gateway = Mock()

    gateway.cobrar.return_value = True

    resultado = processar_pedido(
        100,
        "1111222233334444",
        gateway
    )

    gateway.cobrar.assert_called_once()

    assert resultado == "Compra aprovada!"


def test_gateway_recusado():

    gateway = Mock()

    gateway.cobrar.return_value = False

    with pytest.raises(
        ValueError,
        match="Pagamento recusado"
    ):

        processar_pedido(
            100,
            "1111222233334444",
            gateway
        )