import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# TODO: validar os inputs

# imprima a equação
aSignal = "+ " if a >= 0 else "-"
bSignal = "+ " if b >= 0 else "-"
cSignal = "+ " if c >= 0 else "-"

termo1 = aSignal + str(abs(a)) + "x²" if a != 0 else ""
termo2 = bSignal + str(abs(b)) + "x" if b != 0 else ""
termo3 = cSignal + str(abs(c)) if c != 0 else ""

print("A equação é: y =", termo1, termo2, termo3)

# calcula raízes
delta = b ** 2 - 4 * a * c

if a != 0:
    if delta > 0 :
        x1 = (- b + math.sqrt(delta)) / (2 * a)
        x2 = (- b - math.sqrt(delta)) / (2 * a)
        print("x1 = ", x1)
        print("x2 = ", x2)
    elif delta == 0:
        x = (- b + math.sqrt(delta)) / (2 * a)
        print("x1 = ", x)
    else:
        print("A equação não possui raízes!")
else:
    print("A equação não é do segundo grau!")