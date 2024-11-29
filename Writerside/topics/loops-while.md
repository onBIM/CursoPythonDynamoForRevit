# while

## Descrição

O loop `while` é usado para executar um bloco de código repetidamente enquanto uma condição for verdadeira.

É útil quando você não sabe quantas vezes o loop precisa ser executado.

> É importante garantir que a condição do loop seja alterada em algum momento para evitar um loop infinito.

## Sintaxe

```python
while condicao:
    # Código a ser executado
```

## Exemplos

### Exemplo 1: Contagem regressiva

```python
# inicializa o contador
contador = 5

# enquanto o contador for maior que 0, 
# imprime o valor do contador e decrementa 1
while contador > 0:
    print(contador)
    contador -= 1 # decrementa 1

print("Fim da contagem regressiva.")
```

### Exemplo 2: Encontrar a soma de números de 1 a 10

```python
# inicializa a variável de soma e o número
soma = 0
numero = 1

while numero <= 10:
    soma += numero
    numero += 1
    
print("A soma dos números de 1 a 10 é:", soma)
```

### Exemplo 3: Adivinhar o número secreto

```python
import random

# gera um número aleatório entre 1 e 20
numero_secreto = random.randint(1, 20)

# inicializa o palpite e o contador de tentativas
palpite = None
tentativas = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número secreto (entre 1 e 20): "))
    
    tentativas += 1
    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")

print(
    "Parabéns! Você adivinhou o número secreto" + 
    f"{numero_secreto} em {tentativas} tentativas."
)
```

## Exercícios

### Exercício 1

Imprimindo números pares de 1 a 10

Escreva um programa que imprime os números pares de 1 a 10 usando um loop `while`.

```python
numero = 2
while numero <= 10:
    print(numero)
    numero += 2
```

### Exercício 2

Escreva um programa que solicita ao usuário um número e imprime a tabuada desse número usando um loop `while`.

```python
numero = int(input("Digite um número: "))
multiplicador = 1

while multiplicador <= 10:
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
    multiplicador += 1
```

### Exercício 3

Escreva um programa que solicita ao usuário uma senha e continua solicitando até que a senha digitada seja "python".

```python
senha = ""

while senha != "python":
senha = input("Digite a senha: ")

print("Senha correta!")
```
