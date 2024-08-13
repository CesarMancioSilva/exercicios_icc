# | a b | | e f |  k11=ae+bg k12=af+bh
# | c d | | g h |  k21=ce+dg k22=cf+dh
# matrizA[0][0] = a; matrizA[0][1] = b
# matrizB[0][0] = e ; matrizB[0][1] = f
matrizA = []
matrizB = []
for i in range(4):
    x,y = map(int,input().split())
    if i<=1:
        matrizA.append([x,y])
    else:
        matrizB.append([x,y])

k11 = (matrizA[0][0] * matrizB[0][0]) + (matrizA[0][1] * matrizB[1][0])
k12 = (matrizA[0][0] * matrizB[0][1]) + (matrizA[0][1] * matrizB[1][1])

k21 = (matrizA[1][0] * matrizB[0][0]) + (matrizA[1][1] * matrizB[1][0])
k22 = (matrizA[1][0] * matrizB[0][1]) + (matrizA[1][1] * matrizB[1][1])

print(k11,k12)
print(k21,k22)