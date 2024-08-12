import os
def verificador(intro):
    while True:
        valor = input(intro)
        if valor.isdigit():
            os.system('cls')
            print("O valor inserido precisa ser texto.")
        else:
            return valor

texto = verificador("Insira o texto para a contagem: ")
dicionario ={x:texto.count(x) for x in texto}
for chave,valor in dicionario.items():
    print(f"{chave}: {valor}")
