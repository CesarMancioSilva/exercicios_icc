texto = input().lower().replace(" ","")

resultado = {'Vogal':0,'Consoante':0}
for i in texto:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='á' or i=='é' or i=='í' or i=='ó' or i=='ú':
        resultado['Vogal'] +=1
    else:
        resultado['Consoante'] +=1
print(f"Vogais: {resultado['Vogal']}")
print(f"Consoantes: {resultado['Consoante']}")