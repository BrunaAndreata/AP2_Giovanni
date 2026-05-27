Feature: Compra

Scenario: Compra com sucesso

Given que existe um produto disponível
When o cliente compra o produto
Then a compra deve ser aprovada