import mercadopago


public_key = "APP_USR-3b8cae94-f8bd-4cbd-8cbf-e278f812068d"
token = "APP_USR-5258523380410715-112717-546bf1bd12f8fd29a449cf15187281cb-2120384279"


def criar_pagamento(itens_pedido, link):
    # Adicione as credenciais
    sdk = mercadopago.SDK(token)

    #itens que ele esta comprando no formato de dicionario
    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome_produto = item.itemestoque.produto.nome
        preco_unitario = float(item.itemestoque.produto.preco)
        itens.append({
            "title": nome_produto,
            "quantity": quantidade,
            "unit_price": preco_unitario,
        })

    #valor total
    # Cria um item na preferência
    preference_data = {
        "items": itens,
        "auto_return": "all",
        "back_urls": {
            "success": link,
            "pending": link,
            "failure": link
        }
    }

    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta["response"]["init_point"]
    id_pagamento = resposta["response"]["id"]
    return link_pagamento, id_pagamento
