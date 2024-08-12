entrada = input('Insira a temperatura e a escala: ')
arry_valores = entrada.split()

print(int(9*int(arry_valores[0])/5 +32), "F")
print(int(arry_valores[0]) +273, "K")