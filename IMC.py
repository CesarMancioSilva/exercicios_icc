import os
resultado = []
def question_maker(question):
    while True:
        try:
            value = float(input(question))
            return value
        except:
            print('O valor inserido precisa ser um numero válido.')

for i in range(3):
    altura = question_maker(f"Qual a altura numero {i+1}: ")
    peso = question_maker(f"Qual o peso {i+1}: ")
    os.system('cls')
    resultado.append(round(peso/altura**2,2))

print(resultado[0],resultado[1],resultado[2])