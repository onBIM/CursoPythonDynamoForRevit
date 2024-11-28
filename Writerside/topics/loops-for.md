# for

## Descrição

O laço `for` é utilizado para iterar sobre uma sequência (como uma lista, tupla ou string) ou outros objetos iteráveis.
O formato básico de um laço `for` em Python é:

## Sintaxe

```python
for item in iterável:
    # bloco de código a ser executado para cada item
```

## Exemplos:

### Exemplo 1
Iterando sobre uma lista

```python
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)
```

No exemplo acima, o laço `for` irá imprimir cada item na lista `frutas`.

### Exemplo 2
Usando a função `range`

A função `range` é muito útil para criar sequências de números.

```python
for i in range(5):
    print(i)
```

Este código irá imprimir os números de 0 a 4.

### Exemplo 3
Iterando sobre uma string

```python
palavra = "Python"
for letra in palavra:
    print(letra)
```

O laço acima imprime cada letra da string `palavra`.

### Exemplo 4
Iterando sobre um dicionário

```python
idades = {"Ana": 25, "Pedro": 32, "João": 42}
for nome, idade in idades.items():
    print(f"{nome} tem {idade} anos.")
```

Neste exemplo, o laço `for` percorre as chaves e valores do dicionário `idades` e os imprime.

### Exemplo 5
Uso de `break` e `continue` no `for`:

- **`break`:** Encerra o laço imediatamente.
- **`continue`:** Pula para a próxima iteração.

```python
# Exemplo de break
for num in range(10):
    if num == 5:
        break
    print(num)

# Exemplo de continue
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
```

> `break` e `continue` podem ser usados em loops `for` e `while`.
> 
{style="note"}

O primeiro loop interrompe a execução quando `num` é igual a 5. O segundo loop pula a impressão dos números pares.

## Exercícios

### Exercício 1:

Iterando sobre uma lista

Crie um programa que percorra uma lista de números e imprima o quadrado de cada número.

```python
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero ** 2)
```

### Exercício 2

Utilizand a função `range`

Utilize a função `range` para imprimir os primeiros 10 números pares.

```python
for i in range(0, 20, 2):
    print(i)
```

### Exercício 3

Iterando e modificando um dicionário

Crie um programa que percorra um dicionário de preços de produtos e aplique um desconto de 10% em cada um deles,
imprimindo o novo dicionário com os preços atualizados.

```python
precos = {"produto1": 100, "produto2": 200, "produto3": 300}
novos_precos = {}

for produto, preco in precos.items():
    novos_precos[produto] = preco * 0.9
    
print(novos_precos)
```