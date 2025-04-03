# Crie um dicionário para armazenar informações de um livro, 
# incluindo título, autor e ano de publicação. Imprima cada informação.

from typing import Dict, Any

# livro_01: Dict[str, Any] = {
#     "Titulo" : "O Menino de Asas",
#     "Autor" : "Editoria Vagalume",
#     "Ano" : 1987

# }

# livro_02: Dict[str, Any] = {
#     "Titulo" : "Game Of Thrones",
#     "Autor" : "Lord",
#     "Ano" : 1985

# }

# lista_elementos_livro: list = livro_01.items()
# for elemnto in lista_elementos_livro:
#      #print(elemnto)

            #DICIONARIO DENTRO DE DICIONARIO
lista_livros_com_dict : dict = {
    "livro_01":{ "Titulo" : "O Menino de Asas",
    "Autor" : "Editoria Vagalume",
    "Ano" : 1987},

    "livro_02":{"Titulo" : "Game Of Thrones",
    "Autor" : "Lord",
    "Ano" : 1985}
}

#LENDO VALOR DE INTEM NO DICIONARIO
print(lista_livros_com_dict["livro_01"]["Titulo"])