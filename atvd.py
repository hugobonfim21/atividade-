import requests



resposta =  requests.get(f'https://68d3dbd2214be68f8c677cb9.mockapi.io/Restaurante')

print(resposta.json())

# pedido= input('digite o id do seu pedido para poder deletar')
# requests.delete(f'https://68d3dbd2214be68f8c677cb9.mockapi.io/restauranteef5a150f641654.mockapi.io/Restaurante/{pedido}')

# import requests 

prato = input('digite o que voce quer')
pedido={
    'prato':prato,
    'bebida':'caldo de cana',
    'mesa':'6'
}

requests.post("https://68d3dbd2214be68f8c677cb9.mockapi.io/Restaurante",pedido )

import requests 

resposta = requests.get('https://68d3dbd2214be68f8c677cb9.mockapi.io/restaurante.mockapi.io/Restaurante')

print(resposta.json())

# import requests 
# pedido={
#     'Prato': 'arroz com feijao',
#     'Bebida':'suco',
#     'Mesa': '4'
# }

# requests.put('https://68d3dbd2214be68f8c677cb9.mockapi.io/restaurante.mockapi.io/Restaurante/2',pedido)