# Texto

## Definição no Python

`str()`

Strings são pedaços de texto. 

Elas podem ser definidas por qualquer coisa entre aspas duplas `" "` ou simples `' '`.

Podemos dizer também que strings são uma sequência/_array_ de caracteres. 
Por isso, muitas vezes são tratados dessa forma.

## Operações básicas de string

```python
umastring = "Olá, Mundo!"
```

#### len

Retorna o tamanho da string



```python
print len(umastring)


```

#### index

Retorna o index do caractere na string

```python
print umastring.index("o")
print umastring.index("O")
```

#### count

Conta as ocorrências de um caractere no string

```python
print umastring.count("l")
```

#### slice

Usado para obter uma parte da string (_substring_)

```python
print umastring[3:7]
```

> O `slice` é uma ferramenta também usada em listas para obter uma parte delas (_sublista_).
> 
{style="note"}

#### upper / lower

Muda a capitalização da string para maiúscula ou minúscula, respectivamente.

```python
print umastring.upper()
print umastring.lower()
```

#### startswith / endwith

Indica se uma string começa / termina com a outra string passada como argumento

```python
print umastring.startswith("Olá")
print umastring.endswith("Mundo!")
```

#### split

Divide a string com base no caractere passado como argumento.

```python
umaspalavras = umastring.split(" ")
```

## Exercício {id="eq-segundo-grau-com-texto"}
Melhorar os resultados do exercício da [Equação do Segundo Grau](Número.md#number-exercise)

Os resultados devem mostrar a fórmula da equação e também os resultados das raízes, caso existam.
Se não existirem, o script deve informar que a equação não possui raízes.

Exemplo: a = 1, b = -3 e c = 2

A saída (OUT) deve ser:

y = x² - 3x + 2

x1 = ...

x2= ...

Para determinar se uma equação do segundo grau possui raízes reais, você precisa calcular o discriminante,
também conhecido como delta (Δ). A equação do segundo grau tem a forma geral:

$$ ax^2 + bx + c = 0 $$

Aqui estão os passos para determinar as raízes:

1. **Identifique os coeficientes** (a), (b) e (c) na equação.
2. **Calcule o discriminante** usando a fórmula: $$ Δ = b^2 − 4ac $$
3. **Analise o valor de Δ**:
    *   Se Δ > 0, a equação possui duas raízes reais e distintas.
    *   Se Δ = 0, a equação possui uma raiz real dupla.
    *   Se Δ < 0, a equação não possui raízes reais.

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