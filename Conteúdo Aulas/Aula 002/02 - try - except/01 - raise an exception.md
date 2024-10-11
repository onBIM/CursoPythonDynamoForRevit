# Exceções em Python

## Descrição

É interessante algumas vezes fazermos com que nossos métodos lancem exceções específicas para deixar nosso código mais consistente e fácil e depurar.



Para fazer isso usamos o comando `raise`



O comando `raise` em Python é usado para lançar exceções, permitindo que você interrompa a execução normal do programa e sinalize a ocorrência de um erro.



### Exemplo

Suponha que temos uma função que verifica a idade de uma pessoa e só permite a entrada se a pessoa tiver 18 anos ou mais. Se a idade for menor que 18, a função lançará uma exceção personalizada.

```python
def dividir_numeros(a, b):
    try:
        resultado = a / b
        print(f"O resultado da divisão é: {resultado}")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")

# Exemplo de usodividir_numeros(10, 0)
```

#### Explicação do Código:

1. **Bloco try**:
    *   Tentamos dividir `a` por `b` e armazenar o resultado.
    *   Se a divisão for bem-sucedida, o resultado é impresso.
2. **Bloco except**:
    *   Captura a exceção `ZeroDivisionError` se `b` for zero e imprime uma mensagem de erro apropriada.



## Onde encontrar as exceções mais comuns lançadas pelo Python?



Você pode encontrar uma lista das exceções mais comuns lançadas 
pelo Python na [**documentação oficial do Python**](https://docs.python.org/pt-br/3/library/exceptions.html?formCode=MG0AV3). 

Aqui estão algumas das exceções mais comuns:

*   **`AssertionError`**: Gerada quando uma instrução `assert` falha.
*   **`EOFError`**: Gerada quando a função `input()` atende à condição de fim de arquivo.
*   **`AttributeError`**: Gerada quando uma atribuição ou referência de atributo falha.
*   **`TabError`**: Gerada quando os recuos consistem em tabulações ou espaços inconsistentes.
*   **`ImportError`**: Gerada quando a importação de um módulo falha.
*   **`IndexError`**: Gerada quando um índice está fora do intervalo válido.
*   **`KeyError`**: Gerada quando uma chave não está presente em um dicionário.
*   **`ValueError`**: Gerada quando uma função recebe um argumento de valor incorreto.
*   **`TypeError`**: Gerada quando uma operação é aplicada a um objeto de um tipo inapropriado.
*   **`ZeroDivisionError`**: Gerada quando se tenta dividir por zero.

Essas exceções são padrão no Python e são usadas para lidar com diferentes tipos de erros que 
podem ocorrer durante a execução de um programa.

### Exercício

Melhorar a execução do código de cáculo da equação do segundo grau 
([exercicio - eq segundo grau.py](../../../Python%20Files/Aula%20001/exercicio%20-%20eq%20segundo%20grau.py)), 
lançando exceções específicas para onde houver problemas: