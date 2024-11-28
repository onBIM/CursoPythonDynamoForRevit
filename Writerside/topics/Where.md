# Where

## Definição
O método `Where` é utilizado para filtrar uma sequência de valores com base em um predicado.

<note>Um <b>predicado</b> é uma função que retorna um valor booleano, ou seja, <code>True</code> ou <code>False</code>.</note>

Vimos no tópico [](Template-Python-onBIM.md#importa-os-m-todos-de-extens-o-do-linq)
que para usar os métodos de extensão do **Linq** no IronPython antes precisamos importá-lo.

## Exemplo
```python
import clr

# Adiciona a referência para o System.Core
clr.AddReference("System.Core")

# Importa os métodos de extensão do LINQ.
import System
clr.ImportExtensions(System.Linq)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = numeros.Where(lambda n: n % 2 == 0)

OUT = pares
```

![where-even-numbers.png](where-even-numbers.png) {thumbnail="true"}

Só para exemplificar, veja como ficaria nosso código se utilizássemos uma função convencional ao invés de uma `lambda`.

```python
import clr

# Adiciona a referência para o System.Core
clr.AddReference("System.Core")

# Importa os métodos de extensão do LINQ.
import System
clr.ImportExtensions(System.Linq)

def is_even(n):
	return n % 2 == 0
	
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = numeros.Where(is_even)

OUT = pares
```

<tip>Isso será útil quando precisarmos passar uma função mais complexa.</tip>

<warning>Perceba que ambos os códigos só serão executados se utilizarmos o <b>IronPython</b>.</warning>

Como mostrado na imagem abaixo, veja que se tentarmos executar esse código no **CPython** teremos um erro.
O método `Where` não é reconhecido, uma vez que o **CPython** não funciona com os recursos do .NET como o **Linq**.

![error-running-system-on-cpython.png](error-running-system-on-cpython.png) {thumbnail="true"}

## Exercício

No exemplo mostrado em [](Coleta-de-Elementos.md#usando-um-elementlogicalfilter), onde coletamos todas as _Furnitures_ 
e _Caseworks_ que estão sobre um piso, adapte o código utilzando o método `Where` para 
filtrar somente os elementos que são _Chairs_ (cadeiras).

<chapter title="Solução" collapsible="true" default-state="collapsed">
	<img src="collecting-chairs.png" alt="collecting-chairs.png" thumbnail="true" width="600" style="block"/>
	<p>Veja como ficou o código final 👇</p>
	<code-block src="../resources/python/collecting-chairs.py" lang="Python" collapsible="true" collapsed-title="Código" default-state="collapsed"/>
</chapter>



