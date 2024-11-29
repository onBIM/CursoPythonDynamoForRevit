# tuple

## Definição

Uma **tuple** em Python é uma coleção ordenada e imutável de elementos. Isso significa que, uma vez criada,
você não pode alterar, adicionar ou remover itens dela.

As tuplas são definidas usando parênteses `()` e podem conter elementos de diferentes tipos de dados.

As tuples são uma parte essencial do Python, oferecendo uma maneira eficiente de armazenar e acessar dados que
não precisam ser modificados.

Também podem ser usadas para retornar múltiplos valores de uma função.

## Criando uma Tuple

```python
# Criando uma tuple
minha_tuple = (1, 2, 3, 'a', 'b', 'c')
```

## Acessando Elementos

Você pode acessar elementos de uma tuple usando índices, começando do zero.

```python
# Acessando o primeiro elemento
primeiro_elemento = minha_tuple[0]  # Saída: 1

# Acessando o último elemento
ultimo_elemento = minha_tuple[-1]  # Saída: 'c'
```

## Métodos Principais

Embora as tuples sejam imutáveis, existem alguns métodos úteis:

* `count()`: retorna o número de vezes que um valor aparece na tuple.

```python
# Contando ocorrências de um elemento
ocorrencias = minha_tuple.count('a')  # Saída: 1
```

* `index()`: retorna o índice da primeira ocorrência de um valor.

```python
# Encontrando o índice de um elemento
indice = minha_tuple.index('b')  # Saída: 4
```

## Usos Comuns

As tuples são frequentemente usadas para:

* Armazenar dados que não devem ser alterados.
* Retornar múltiplos valores de uma função.

```python
# Retornando múltiplos valores de uma função
def coordenadas():
    return (10, 20)

x, y = coordenadas()
```
