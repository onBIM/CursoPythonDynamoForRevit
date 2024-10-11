# Coleções de dados no System

## Listas - `List<T>`

A coleção `List<T>` do namespace `System.Collections.Generic` em C# é uma classe que 
**representa uma lista** **fortemente tipada** **de objetos acessíveis por índice**. 

Ela é usada para armazenar e manipular uma coleção de elementos de um tipo específico, 
oferecendo flexibilidade e eficiência.

### Para que serve

A `List<T>` é útil quando você precisa de uma coleção que pode crescer e diminuir dinamicamente, ao contrário de arrays que têm tamanho fixo. Ela é amplamente utilizada devido à sua capacidade de adicionar, remover e acessar elementos de forma eficiente.

### Principais Propriedades

**`Count`**: Retorna o número de elementos atualmente na lista.

**`Capacity`**: Indica o número de elementos que a lista pode conter antes de precisar redimensionar internamente.

### Principais Métodos

> #### **`Add(T item)`**: Adiciona um objeto ao final da lista

C#

```csharp
List<int> numeros = new List<int>();
numeros.Add(1);
numeros.Add(2);
```

IronPython

```python
 numeros = SystemList[int]()
 numeros.Add(1)
 numeros.Add(2)
```

> #### **`AddRange(IEnumerable<T> collection)`**: Adiciona os elementos de uma coleção ao final da lista

C#

```csharp
List<int> maisNumeros = new List<int> { 3, 4, 5 };
numeros.AddRange(maisNumeros);
```

IronPython

```python
maisNumeros  = SystemList[int]([ 3, 4, 5 ])
numeros.AddRange(maisNumeros)
```

Neste exemplo, os elementos da lista `maisNumeros` são adicionados ao final da lista `numeros`, resultando em uma lista que contém os elementos 2, 3, 4, e 5.

> #### **`Remove(T item)`**: Remove a primeira ocorrência de um objeto específico da lista

C#

```csharp
numeros.Remove(1);
```

IronPython

```python
numeros.Remove(1)
```

> #### **`Contains(T item)`**: Verifica se um elemento está na lista

C#

```csharp
bool existe = numeros.Contains(2); // retorna true
```

IronPython

```python
existe = numeros.Contains(2) # retorna True
```

> #### **`IndexOf(T item)`**: Retorna o índice da primeira ocorrência de um elemento

C#

```csharp
int indice = numeros.IndexOf(2); // retorna 0
```

IronPython

```python
indice = numeros.IndexOf(2) # retorna 0
```

> #### **`Insert(int index, T item)`**: Insere um elemento na lista na posição especificada

C#

```csharp
numeros.Insert(0, 3); // insere 3 na posição 0
```

IronPython

```python
numeros.Insert(0, 3) # insere 3 na posição 0
```

> #### **`Sort()`**: Ordena os elementos da lista

C#

```scss
numeros.Sort();
```

IronPython

```python
numeros.Sort()
```

> #### **`Clear()`**: Remove todos os elementos da lista

C#

```scss
numeros.Clear();
```

IronPython

```python
numeros.Clear()
```
