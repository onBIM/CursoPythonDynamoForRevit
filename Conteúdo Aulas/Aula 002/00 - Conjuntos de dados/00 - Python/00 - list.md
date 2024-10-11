# Coleções de dados em Python

## Listas (list)

![python_list.png.](images/list.png)

### Definição

Uma lista em Python é uma coleção ordenada de elementos que pode conter itens de tipos diferentes,
como números, strings ou até outras listas.

Os items da lista são numerados começando do '0' (zero)

As listas são mutáveis, o que significa que você pode alterar seus elementos após a criação.

Elas são definidas usando colchetes `[]`.

### Exemplos de criação de lista

```python
# Criando uma lista de números
numeros = [1, 2, 3, 4, 5]

# Criando uma lista de strings
frutas = ["maçã", "banana", "cereja"]

# Lista mista
mista = [1, "dois", 3.0, [4, 5]]

# Criando uma lista vazia
lista_vazia1 = []
lista_vazia2 = list()
```

### Principais métodos e propriedades

* **Acessar elementos**: Você pode acessar elementos individuais usando índices, começando do zero.

```python
primeiro_numero = numeros[0]  # 1
primeira_fruta = frutas[0]    # "maçã"
```

* **Adicionar elementos**: Use `append()` para adicionar um elemento ao final da lista.

```python
frutas.append("laranja")
# frutas agora é ["maçã", "banana", "cereja", "laranja"]
```

* **Inserir elementos**: Use `insert()` para adicionar um elemento em uma posição específica.

```python
numeros.insert(2, 10)
# numeros agora é [1, 2, 10, 3, 4, 5]
```

* **Remover elementos**: Use `remove()` para remover a primeira ocorrência de um valor.

```python
frutas.remove("banana")
# frutas agora é ["maçã", "cereja", "laranja"]
```

* **Remover por índice**: Use `pop()` para remover um elemento pelo índice e retornar o elemento removido.

```python
ultimo_numero = numeros.pop()
# ultimo_numero é 5, numeros agora é [1, 2, 10, 3, 4]
```

* **Tamanho da lista**: Use `len()` para obter o número de elementos na lista.

```python
tamanho = len(frutas)  # 3
```

* **Ordenar lista**: Use `sort()` para ordenar a lista em ordem crescente.

```python
numeros.sort()
# numeros agora é [1, 2, 3, 4, 10]
```

* **Reverter lista**: Use `reverse()` para inverter a ordem dos elementos.

```python
numeros.reverse()
# numeros agora é [10, 4, 3, 2, 1]
```
