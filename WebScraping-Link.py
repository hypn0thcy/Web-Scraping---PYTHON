import re
import requests

print("\n  [$] Buscador De Links [$]")
print("\n    @Created BY: hypn0thcy\n")

try:
    url = str(input("Qual o Alvo? -> "))
    requisicao = requests.get(url)
    padrao = re.findall(r'http.://[\w-]+\.[\w\.-]+/[\w-]+', requisicao.text)

    if padrao:
        print('\nLinks -> ', padrao)
    else:
        print("\nNão Foi Encontrado!")
except Exception as erro:
    print("\n[!] Houve Algum erro -> ", erro)
