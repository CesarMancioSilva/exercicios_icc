texto = input("Insira o texto para contagem: ")
separacao = texto.split()
dicionario={}
for x in separacao:
  i=0
  for z in separacao:
    if x == z:
      i+=1
  dicionario[x] = i
for chave,valor in dicionario.items():
  print(f"{chave}: {valor}")
