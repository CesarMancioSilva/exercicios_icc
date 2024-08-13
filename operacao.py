texto = input()
if texto[1] == "*":
    print(f"{texto}={int(texto[0])*int(texto[2])}")
elif texto[1]=="^":
    print(f"{texto}={int(texto[0])**int(texto[2])}")
elif texto[1] == "/":
    print(f"{texto}={int(texto[0])/int(texto[2])}")
