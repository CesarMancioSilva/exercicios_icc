n = int(input("Numero para fatorar: "))
result=1
for i in range(n):
    result*=n-i
print(result)