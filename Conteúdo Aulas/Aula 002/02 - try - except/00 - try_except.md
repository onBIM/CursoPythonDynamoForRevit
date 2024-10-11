# Exceções em Python

## Descrição

Em Python, exceções são erros detectados durante a execução de um programa.

Elas permitem que você lide com erros de uma maneira controlada, separando o código de tratamento de erros do código principal.

### Vantagens de usar exceções:

1. **Clareza e Manutenção**: As exceções permitem que o fluxo de controle do programa permaneça claro, com o código
   principal focado na execução normal e o tratamento de erros localizado em blocos específicos.
2. **Tratamento Localizado**: As exceções permitem o tratamento de erros em níveis superiores da pilha de chamadas, em
   vez de exigir a verificação de erros em cada ponto onde algo pode dar errado.
3. **Recuperação de Erros**: Elas oferecem uma maneira estruturada de lidar com falhas permitindo que o programa tente
   uma recuperação ou término gracioso.

### Desvantagens de usar exceções:

1. **Desempenho**: O uso de exceções pode ter um impacto no desempenho, especialmente em seções de código executadas com frequência, devido ao custo de lançar e capturar exceções.
2. **Complexidade**: A introdução de muitas exceções pode tornar o código mais difícil de entender e manter,
   especialmente em sistemas complexos.
3. **Ocultação de Erros**: Se usadas indevidamente, exceções podem ocultar erros, dificultando diagnosticar
   problemas reais no código.

Exemplo básico de tratamento de exceção:

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    resultado = None
    
print("Erro: Divisão por zero não é permitida.")
```

O bloco try tenta executar o código problemático, enquanto o bloco except trata a exceção específica do erro `ZeroDivisionError`.

## Capturando uma exceção específica

Para capturar uma exceção específica, você pode usar a sintaxe `except` seguida pelo nome da exceção.

```python
try:
    # Código problemático
except NomeDaExcecao:
    # Tratamento da exceção
```

### Exemplo

Podemos criar um bloco de código que seja executado caso uma exceção específica ocorra. 

Veja um exemplo abaixo de como fazer isso:

```python
def calcular_media_lista(valores):
    try:
        numeros = [int(valor) for valor in valores]
        media = sum(numeros) / len(numeros)
        print(f"A média dos números é: {media}")

    except ValueError as e:
        print(f"Erro: A lista contém dados não numéricos. Detalhes: {e}")
    except ZeroDivisionError:
        print("Erro: Não é possível calcular a média de uma lista vazia.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Testando com uma lista contendo valores inválidos
valores = ["10", "20", "abc", "30"]
calcular_media_lista(valores)

# Testando com uma lista vazia
valores = []
calcular_media_lista(valores)
```

