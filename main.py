# Módulo
# Requisitos:
# Autor: Jessica Prass
# Versão: 0.0.1
# Data: 06/09/2022

# Importando o pacote requests
import requests

# Lendo a página de política do G1
endereco = "https://g1.globo.com/politica/"
pagina = requests.get(endereco)
pagina.status_code

# Gravando o arquivo com as informações da variável pagina
arquivo = open('pagina.html', 'wb')
# w = texto
# wb = vários dados no mémoria, bytes
for texto in pagina.iter_content(1048576)
    # quantidade de bits lidos de cada vez
    arquivo.write(texto)
arquivo.close()