# OrderBy

## Definição

O método `OrderBy` é utilizado para **ordenar** os elementos de uma coleção.

## Exemplo

Vamos supor que tenhamos uma lista de pessoas e queremos ordená-las pelo nome.

Usando o método `OrderBy` do **Linq** podemos fazer isso de forma muito mais eficiente e simples, 
sem a necessidade de usar um laço `for`.

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

# ordena as pessoas pelo nome
pessoas_ordenadas = pessoas.OrderBy(lambda p: p.nome)

OUT = pessoas_ordenadas.Select(lambda p: f"{p.nome} - {p.idade} anos")
```

![linq-orderby-people-byname.png](linq-orderby-people-byname.png) {thumbnail="true" width="700"}

> Se quisermos ordenar as pessoas pelo nome de forma decrescente, podemos usar o método `OrderByDescending`.
> 
{style="note"}

```python
# ordena as pessoas pelo nome de forma decrescente
pessoas_ordenadas = pessoas.OrderByDescending(lambda p: p.nome)
```

## Exercício

Colete os Rooms do **Level 1** do modelo **rac_basic_sample_project_rvt** e ordene-os pelo nome.

<chapter title="Solução" collapsible="true" default-state="collapsed">
	<code-block src="../resources/python/collect-rooms-ordered-by-name.py" 
				lang="Python"
				collapsible="true" 
				collapsed-title="Código principal" 
				default-state="collapsed"
				include-lines="53-56,74-76,88-93,103-131"/>
	<img src="collect-rooms-ordered-by-name.png" 
         alt="collect-rooms-ordered-by-name" 
         thumbnail="true" 
         style="block"
         width="700" />
	<br/>
	<p>Baixe o código completo aqui 👉 <resource src="collect-rooms-ordered-by-name.py"/></p>
</chapter>