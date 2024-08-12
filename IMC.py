def question_maker(question):
    while True:
        try:
            value = int(input(question))
            return value
        except:
            print('O valor inserido precisa ser um numero válido.')
            
resultado = []
size = question_maker("Quantos IMC você irá calcular? ")
for i in range(size):
    entrada = input(f"Qual a altura e peso numero {i+1}: ")
    stage = entrada.split(',')
    resultado.append(round(float(stage[1])/float(stage[0])**2,2))
    
texto = ''
for z in range(size):
    if z == size-1:
        texto+= f'{resultado[z]}'
    else:
        texto+= f'{resultado[z]} '

print(texto)
