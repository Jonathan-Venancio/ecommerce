import requests
from django.conf import settings

VENDUS_API_KEY = settings.VENDUS_API_KEY
VENDUS_API_BASE_URL = settings.VENDUS_API_BASE_URL

# Função para listar clientes
#def listar_clientes():
#    url = "https://www.vendus.pt/ws/v1.1/clients/?api_key=018e1c2f5799590b8b0d1cad2e088dc1"
#    headers = {
#        "Authorization": f"Bearer {VENDUS_API_KEY}",
#        "Content-Type": "application/json"
#    }
#    params = {"page": 23}
#    response = requests.get(url, headers=headers, params=params)
#    response.raise_for_status()  # Lança um erro para códigos de status HTTP de erro
#    return response.json()

def listar_clientes(pagina=1):
    url = "https://www.vendus.pt/ws/v1.1/clients/"
    headers = {
        "Authorization": f"Bearer {VENDUS_API_KEY}",
        "Content-Type": "application/json"
    }
    params = {"api_key": "018e1c2f5799590b8b0d1cad2e088dc1", "page": pagina}
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Lança erro se houver problema na requisição
    
    clientes = response.json()  # Lista de clientes é a resposta direta
    
    # Estabelece controle de navegação de páginas
    tem_proxima_pagina = len(clientes) > 0  # Se a resposta não estiver vazia, pode haver próxima página
    tem_pagina_anterior = pagina > 1  # Página anterior só existe se a página atual for maior que 1

    return {
        "clientes": clientes,
        "pagina_atual": pagina,
        "proxima_pagina": pagina + 1 if tem_proxima_pagina else None,
        "pagina_anterior": pagina - 1 if tem_pagina_anterior else None,
    }