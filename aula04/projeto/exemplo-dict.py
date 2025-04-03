import json

produto_01  = {
    "nome": "sapato",
    "quantidade": 39,
    "preco": 10.38,
    "disponibilidade": True

}

produto_02  = {
    "nome": "smart_tv",
    "quantidade": 20,
    "preco": 2.500,
    "disponibilidade": False

}
carrinho = []

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)

print(carrinho_json)