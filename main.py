# Programa principal
# Requisitos: Coleta dados de nóticias políticas na página G1 e os salva em um arquivo no formato html.
# Autor: Jessica Prass
# Versão: 1.0.0
# Data: 06/09/2022

import requests

# Lendo a página de política do G1
endereco = "https://g1.globo.com/politica/"
pagina = requests.get(endereco)
pagina.status_code

# Gravando o arquivo com as informações da variável pagina
arquivo = open('pagina.html', 'wb')

for texto in pagina.iter_content(1048576):
    # quantidade de bits lidos de cada vez
    arquivo.write(texto)
arquivo.close()
