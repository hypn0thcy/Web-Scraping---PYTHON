import re
import requests

print("\n  [$] Buscador De Telefones [$]")
print("\n     @Created BY: hypn0thcy\n")

try:
    url = str(input("Qual o Alvo? -> "))
    requisicao = requests.get(url)
    padrao = re.findall(r'[(\d\d)]+[\0-5\d]+[\0-5]+', requisicao.text)

    if padrao:
        print('\nTelefones -> ', padrao)
    else:
        print("\nNão Foi Encontrado!")
except Exception as erro:
    print("\n[!] Houve Algum erro -> ", erro)
