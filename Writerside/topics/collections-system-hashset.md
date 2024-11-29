# HashSet

## Definição

A coleção `HashSet<T>` do namespace `System.Collections.Generic` em C# é uma classe que
**representa um conjunto fortemente tipado de elementos sem duplicatas**.

Ela é usada para armazenar e manipular uma coleção de elementos únicos de um tipo específico,
oferecendo operações de conjunto eficientes.

O `HashSet<T>` é útil quando você precisa de uma coleção que garante a ausência de duplicatas e fornece desempenho
eficiente para operações como adição, remoção e verificação de elementos.

Para utilizarmos o `HashSet<T>` no IronPython, precisamos importar a classe `HashSet`
do namespace `System.Collections.Generic`.

```python
import clr
clr.AddReference("System.Core")
from System.Collections.Generic import HashSet
```

## Principais Propriedades

**`Count`**: Retorna o número de elementos atualmente no conjunto.

## Principais Métodos

### `Add(T item)`
Adiciona um objeto ao conjunto, se ele ainda não estiver presente, 
retornando um valor booleano indicando se a operação foi bem-sucedida.

C#

```C#
HashSet<int> numeros = new HashSet<int>();
numeros.Add(1); // retorna true
numeros.Add(2); // retorna true
```

IronPython

```python
numeros = HashSet[int]()
numeros.Add(1) # retorna True
numeros.Add(2) # retorna True
```

### `Remove(T item)`
Remove um elemento do conjunto.

C#

```C#
numeros.Remove(1); // retorna true
```

IronPython

```python
numeros.Remove(1) # retorna True
```

### `Contains(T item)`
Verifica se um elemento está presente no conjunto.

C#

```C#
bool existe = numeros.Contains(2); // retorna true
```

IronPython

```python
existe = numeros.Contains(2) # retorna True
```

### `UnionWith(IEnumerable<T> other)`
Modifica o conjunto atual para que ele contenha todos os elementos presentes no conjunto atual e na coleção especificada.

C#

```C#
HashSet<int> maisNumeros = new HashSet<int> { 3, 4, 5 };
numeros.UnionWith(maisNumeros);
```

IronPython

```python
maisNumeros = HashSet[int]([3, 4, 5])
numeros.UnionWith(maisNumeros)
```

### `IntersectWith(IEnumerable<T> other)`
Modifica o conjunto atual para que ele contenha apenas elementos que também estão na coleção especificada.

C#

```C#
HashSet<int> outrosNumeros = new HashSet<int> { 2, 3 };
numeros.IntersectWith(outrosNumeros);
```

IronPython

```python
outrosNumeros = HashSet[int]([2, 3])
numeros.IntersectWith(outrosNumeros)
```

### `ExceptWith(IEnumerable<T> other)`
Remove todos os elementos do conjunto atual que estão na coleção especificada.

C#

```C#
HashSet<int> excecaoNumeros = new HashSet<int> { 2, 5 };
numeros.ExceptWith(excecaoNumeros);
```

IronPython

```python
excecaoNumeros = HashSet[int]([2, 5])
numeros.ExceptWith(excecaoNumeros)
```

###`Clear()`**: Remove todos os elementos do conjunto.

C#

```C#
numeros.Clear();
```

IronPython

```python
numeros.Clear()
```