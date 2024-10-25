# Número

## int

Números inteiros: `int()`

## float

Números decimais: `float()`

## Operações Matemáticas Básicas

*   Soma `+`
*   Subtração `-`
*   Multiplicação `*`
*   Divisão `/`
*   Divisão inteira `//`
*   Resto `%`

### Exemplos

```python
# Soma
a = 10
b = 20
c = a + b
print(c) # 30

# Subtração
a = 10
b = 20
c = a - b
print(c) # -10

# Multiplicação
a = 10
b = 20
c = a * b
print(c) # 200

# Divisão
a = 10
b = 20
c = a / b
print(c) # 0.5

# Divisão inteira
a = 7
b = 3
c = a // b
print(c) # 2

# Resto
a = 5
b = 2
c = a % b
print(c) # 1
```

## Funções Matemáticas

### Usando diretamente o módulo **Python**

```python
import math
```

Exemplo:

```python
# Usando a função sqrt
a = 25
b = math.sqrt(a)
print(b) # 5.0
```

### Usando a Lib do **Dynamo**

```python
# Import Dynamo Library Nodes - Core
import clr
clr.AddReference('DSCoreNodes')
from DSCore import Math as DynamoMath
```

Exemplo:

```python
# Usando a função Sqrt
a = 25
b = DynamoMath.Sqrt(a)
print(b) # 5.0
```

### Usando a Lib do **System** 

> Somente no IronPython
> 
{style="warning"}

```python
# Import System Libraries
import clr
clr.AddReference("System.Core")
from System import Math as SystemMath
```

Exemplo:

```python
# Usando a função Sqrt
a = 25
b = SystemMath.Sqrt(a)
print(b) # 5.0
```

## Exercício

Fazer um script para calcular as raízes de uma equação do segundo grau.

O usuário deve entrar com os valores de **a**, **b** e **c**.

O script deve retornar as raízes.

Lembrando que a fórmula para calcular as raízes é:

$$ \Delta = b^2 - 4ac $$

$$ x = \frac{-b \pm \sqrt{\Delta}}{2a} $$

```python
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
```
{collapsed-title="Solucão" collapsible="true" default-state="collapsed"}