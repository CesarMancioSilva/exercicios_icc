def verificador(text):
    while True:
        x = input(text)
        if x == '':
            print("Erro: entrada inválida, por favor insira uma palavra ou frase")
        else:
            return x

texto = verificador("Insira o texto para identificar se é um palíndromo: ")
texto = texto.replace(" ","")
texto = texto.lower()
if len(texto)%2==0:
    size = int(len(texto)/2)
else:
    size = int(len(texto)/2) + 1

result = []


for z in range(size):
    if texto[z] == texto[-(z+1)]:
        # print(f"True: {texto[z]}={texto[-(z+1)]}")
        result.append(True)
    else:
        # print(f"False: {texto[z]}!={texto[-(z+1)]}")
        result.append(False)

def verificador(array):
    for x in result:
        if x == False:
            return False
if verificador(result)!= False:
    print("É palíndromo")
else:
    print("Não é palíndromo")