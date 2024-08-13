x,y = map(int,input().split())
resultados=[]
for i in range(y-x-1):
    x+=1
    if x%7==0 and x%5==0:
        resultados.append(str(x))
print(','.join(resultados))