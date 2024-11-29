# FirstOrDefault

## Definição

O método `FirstOrDefault` é utilizado para **retornar o primeiro elemento** de uma coleção ou o 
**primeiro elemento que satisfaça uma condição**.

Caso a coleção esteja vazia, ou não exista um elemento que satisfaça a condição, o método retorna `None`.

## Exemplos

A forma mais simples de usar o método `FirstOrDefault` é sem passar nenhum argumento. Nesse caso, o método 
retorna o primeiro elemento da coleção.

```python
import clr

# Adiciona a referência para o System.Core
clr.AddReference("System.Core")

# Importa os métodos de extensão do LINQ.
import System
clr.ImportExtensions(System.Linq)

# cria uma lista de números
numeros = [1, 2, 3, 4, 5]

# retorna o primeiro número da lista
numero = numeros.FirstOrDefault()

OUT = numero # retorna 1
```

Vamos supor que tenhamos uma lista de pessoas e queremos retornar a primeira cujo nome comece com a letra "P".

```python
import clr

# Adiciona a referência para o System.Core
clr.AddReference("System.Core")

# Importa os métodos de extensão do LINQ.
import System
clr.ImportExtensions(System.Linq)

class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

# cria uma lista de pessoas
pessoas = [
	Pessoa("Maria", 30),
	Pessoa("João", 25),
	Pessoa("José", 20),
	Pessoa("Ana", 35),
	Pessoa("Pedro", 40),
	Pessoa("Carla", 45)
]

# retorna a primeira pessoa que o nome comece com a letra "P"
pessoa = pessoas.FirstOrDefault(lambda p: p.nome.startswith('P'))

OUT = f"{pessoa.nome} - {pessoa.idade} anos"
```

![person-with-name-starting-with-p.png](person-with-name-starting-with-p.png) {thumbnail="true" width="700"}

Agora suponha que queremos a pessoa mais nova da lista.

```python
# retorna a pessoa mais nova
pessoa = \
	pessoas \
	.OrderBy(lambda p: p.idade) \
	.FirstOrDefault()
```

> Se quisermos retornar o **último** elemento da coleção, podemos usar o método `LastOrDefault()`.
> 
> Seu funcionamento é similar ao `FirstOrDefault`, mas retorna o último elemento da coleção.
> 
{style="note"}

## Exercício

Obtenha o **Room** do modelo **rac_basic_sample_project_rvt** que se chama **Master Bath**.

> Atenção para o nome do Room, pois ele é [**case-sensitive**](https://pt.wikipedia.org/wiki/Case-sensitive) 
> e também pode não ser exatamente **Master Bath**.
> 
{style="warning"}

<chapter title="Solução" collapsible="true" default-state="collapsed">
	<code-block src="../resources/python/collect-room-master-bath.py"
				collapsible="true"
				collapsed-title="Código principal"
				default-state="collapsed"
				include-lines="64-68"/>
	<img src="collect-room-master-bath.png" alt="room-master-bath.png" width="700" thumbnail="true"/>
	<br/>
	<p>Baixe o código completo aqui 👉 <resource src="collect-room-master-bath.py"/></p>
</chapter>
