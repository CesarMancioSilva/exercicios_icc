x = int(input())
inicio=0
n=1
resultado=[]
for i in range(x):
    resultado.append(str(inicio))
    n,inicio = inicio+n,n
print(" ".join(resultado))