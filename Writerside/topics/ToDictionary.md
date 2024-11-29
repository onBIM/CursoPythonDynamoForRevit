# ToDictionary

## Definição

O método `ToDictionary` é uma extensão do **Linq** utilizado para converter uma coleção de objetos em um dicionário.

## Exemplo

Suponha que temos uma lista de pessoas e queremos converter essa lista em um dicionário 
onde a chave é o nome da pessoa e o valor é a idade da pessoa.

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

# converte a lista de pessoas em um dicionário
dicionario = pessoas.ToDictionary(lambda p: p.nome, lambda p: p.idade)

OUT = dicionario
```

![linq-dictionary-of-people.png](linq-dictionary-of-people.png) {width="700" thumbnail="true"}

> Perceba que passamos duas funções `lambda` para o método `ToDictionary`. 
> - A primeira função é responsável por definir a **chave** do dicionário
> - A segunda função é responsável por definir o **valor** do dicionário.
> 
{style="note"}

> Lembre-se que no Dynamo é obrigatório que as chaves do dicionário sejam `strings`.
> 
{style="warning"}

> Você pode internamento no seu código Python utilizar dicionários com chaves de outros tipos. 
> Porém, ao passar um dicionário para o Dynamo através da porta `OUT` do node Python Script, as chaves devem ser `strings`.

Comentamos sobre dicionários no tópico [](collections.md), da **Aula 002**.

Como mostrado lá, podemos usar dicionários tanto do Python, quanto do .NET. Porém, é importante lembrar que:

> O método `ToDictionary` é uma extensão do **Linq**, portanto, retorna um dicionário do .NET.
> 
{style="warning"}

## Exercício

Crie um dicionário de Rooms, onde:

- a chave é o nome do Room
- o valor é o Elemento Room

<chapter title="Solução" collapsible="true" default-state="collapsed">
	<code-block src="../resources/python/rooms-dictionary.py"
				collapsible="true"
				collapsed-title="Código principal"
				default-state="collapsed"
				include-lines="64-71"/>
	<img src="linq-rooms-dictionary.png" alt="linq-rooms-dictionary" width="700" thumbnail="true"/>
	<br/>
	<p>Baixe o código completo aqui 👉 <resource src="rooms-dictionary.py"/></p>
</chapter>