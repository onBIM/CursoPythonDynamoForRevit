# Coleções de dados em Python

## Conjuntos (set)

### Definição

Um **set** em Python é uma coleção não ordenada de elementos únicos.

Ele é útil quando você precisa armazenar itens sem duplicatas e não se importa com a ordem deles.

### Criando um `set`

Você pode criar um set usando chaves `{ }` ou a função `set()`.

```python
# Usando chaves
meu_set = {1, 2, 3, 4}

# Usando a função set()
outro_set = set([1, 2, 3, 4])
```

### Principais Métodos e Propriedades

#### Adicionar Elementos

Use o método `add()` para adicionar um único elemento.

```python
meu_set.add(5)
```

#### Remover Elementos

Use o método `remove()` para remover um elemento específico. 

> Gera um erro se o elemento não existir.

```python
meu_set.remove(3)
```

```python
meu_set.discard(10)
```

#### União de Sets

Use o método `union()` ou o operador `|` para unir dois sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

uniao = set1.union(set2)
# ou
uniao = set1 | set2
```

#### Interseção de Sets

Use o método `intersection()` ou o operador `&` para encontrar elementos comuns.

```python
intersecao = set1.intersection(set2)
# ou
intersecao = set1 & set2
```

#### Diferença de Sets

Use o método `difference()` ou o operador `-` para encontrar elementos que estão em um set, mas não em outro.

```python
diferenca = set1.difference(set2)
# ou
diferenca = set1 - set2
```

#### Verificar Subset

Use o método `issubset()` para verificar se um set é subconjunto de outro.

```python
set3 = {1, 2}
resultado = set3.issubset(set1)
```