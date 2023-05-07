
# pip --version
# pip --hep

import requests

response = requests.get('http://viacep.com.br/ws/01001000/json/')
print(response.status_code) # foi encontrato com sucesso (200) ou deu erro (400)

#print(response.text)

print(response.json())

dados_cep = response.json()
print(dados_cep['logradouro'])

def retorna_dados_pokemon(pokemon):
    response = requests.get('http://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('http://globallabs.academy/')
    print(response)
