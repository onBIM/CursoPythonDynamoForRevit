# Dictionary

## Definição
A coleção `Dictionary<TKey, TValue>` do namespace `System.Collections.Generic` em C# é uma classe que 
**representa uma coleção de pares chave-valor**.

É usada para armazenar e manipular dados que podem ser acessados por uma chave exclusiva.
A `Dictionary<TKey, TValue>` é útil quando você precisa de uma coleção onde cada elemento possui uma chave única 
associada a ele, permitindo acesso rápido e eficiente aos valores por meio das chaves.

Para utilizarmos o `Dictionary<TKey, TValue>` no IronPython, precisamos importar a classe `Dictionary`
do namespace `System.Collections.Generic`.

```python
import clr
clr.AddReference("System.Core")
from System.Collections.Generic import Dictionary
```

## Principais Propriedades
### `Count` 
Retorna o núme ro de pares chave-valor atualmente no dicionário.

C#

```c#
int count = dic.Count; // retorna 2
```

Python

```python
count = dic.Count # retorna 2
```

### `Keys` e `Values`
Propriedades que retornam, respectivamente, uma coleção das chaves e dos valores no dicionário.

C#

```c#
Dictionary<int, string>.KeyCollection chaves = dic.Keys;
Dictionary<int, string>.ValueCollection valores = dic.Values;
```

Python

```python
chaves = dic.Keys
valores = dic.Values
```

## Principais Métodos

### `Add(TKey key, TValue value)`
Adiciona um par chave-valor ao dicionário.

C#

```c#
Dictionary<int, string> dic = new Dictionary<int, string>();
dic.Add(1, "Um");
dic.Add(2, "Dois");
```    

Python

```python
dic = Dictionary[int, str]()
dic.Add(1, "Um")
dic.Add(2, "Dois")
```

### `Remove(TKey key)`
Remove o par chave-valor associado à chave especificada.
C#

```c# 
dic.Remove(1);
```

Python

```python
dic.Remove(1)
```

### `ContainsKey(TKey key)`
Verifica se o dicionário contém a chave especificada.

C#

```c#
bool existe = dic.ContainsKey(2); // retorna true
```

Python

```python
existe = dic.ContainsKey(2) # retorna True
```

### `ContainsValue(TValue value)`

Verifica se o dicionário contém o valor especificado.

C#

```c#
bool existe = dic.ContainsValue("Dois"); // retorna true
```

Python

```python
existe = dic.ContainsValue("Dois") # retorna True
```

### `Clear()`
Remove todos os pares chave-valor do dicionário.

C#

```c#   
dic.Clear();
```

Python

```python
dic.Clear()
```