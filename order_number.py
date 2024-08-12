import os

def start():
    process = False
    while process == False:
        valor = input("Insira uma sequencia de numeros separados por um espaço: ")
        arry_valor = valor.split()
        process = verify_legit(arry_valor)
    return arry_valor

def verify_legit(array):
    for x in array:
        if x.isdigit() == False:
            os.system('cls')
            print("Todos os caracteres precisam ser numeros.")
            return False
        
resultado = start()
resultado = list(map(int,resultado))
resultado.sort()
resultado = list(map(str,resultado))
text = ''
for i in resultado:
    text += i+' '
print(text)