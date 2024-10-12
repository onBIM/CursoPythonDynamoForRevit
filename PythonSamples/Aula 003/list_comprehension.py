import math

def validateInputs(a, b, c):
    if a == 0 and b == 0 and c == 0:
        raise ValueError("A equação não pode ser resolvida!")
    
    if a == 0:
        raise ValueError("O coeficiente a não pode ser zero!")
    
def imprimeEquacao(a, b, c):
    # imprima a equação
    aSignal = "+ " if a >= 0 else "-"
    bSignal = "+ " if b >= 0 else "-"
    cSignal = "+ " if c >= 0 else "-"
    
    termo1 = aSignal + str(abs(a)) + "x²" if a != 0 else ""
    termo2 = bSignal + str(abs(b)) + "x" if b != 0 else ""
    termo3 = cSignal + str(abs(c)) if c != 0 else ""

    print("A equação é: y =", termo1, termo2, termo3)

def calculaRaizes(a, b, c):
    # calcula raízes
    delta = b ** 2 - 4 * a * c

    if delta > 0 :
        x1 = (- b + math.sqrt(delta)) / (2 * a)
        x2 = (- b - math.sqrt(delta)) / (2 * a)
        return x1, x2
    
    if delta == 0:
        x = (- b + math.sqrt(delta)) / (2 * a)
        return x
    
    return None

try:
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))
    
    validateInputs(a, b, c)
    
    imprimeEquacao(a, b, c)
    
    raizes = calculaRaizes(a, b, c)
    
    print(raizes)
    
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
