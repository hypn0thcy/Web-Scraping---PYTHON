import re
import requests

print("\n  [$] Buscador De Emails [$]")
print("\n    @Created BY: hypn0thcy\n")

try:
    url = str(input("Qual o Alvo? -> "))
    requisicao = requests.get(url)
    padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)

    if padrao:
        print('\nEmails -> ', padrao)
    else:
        print("\nNão Foi Encontrado!")
except Exception as erro:
    print("\n[!] Houve Algum erro -> ", erro)
