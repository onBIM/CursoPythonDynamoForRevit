# List Comprehension

## Definição

List comprehension é uma forma concisa de **criar** listas em Python.

É uma técnica muito poderosa e útil que permite criar listas de forma mais simples e elegante.

## Sintaxe

```python
[expressao for item in iterável if condicao]
```
![loops-list-comprehension.png](loops-list-comprehension.png)

## Exemplos

### Exemplo 1

Gerar uma lista de números pares de 0 a 10

```python
pares = [num for num in range(11) if num % 2 == 0]

print(pares)
```

### Exemplo 2

Gerar uma lista de quadrados dos números de 1 a 5

```python
quadrados = [num ** 2 for num in range(1, 6)]

print(quadrados)
```

### Exemplo 3

Gerar uma lista de frutas com a primeira letra maiúscula

```python
frutas = ["maçã", "banana", "cereja"]

frutas_maiusculas = [fruta.capitalize() for fruta in frutas]

print(frutas_maiusculas)
```

### Exemplo 4

Criar uma matriz 3x4

```python
matriz = [[i * j for j in range(1, 5)] for i in range(1, 4)]

print(matriz)
```
