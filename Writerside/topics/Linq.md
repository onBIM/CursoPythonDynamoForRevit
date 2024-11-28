# Linq

## Definição

Segundo a [documentação oficial da microsoft](https://learn.microsoft.com/en-us/dotnet/csharp/linq/), 
**Linq** (_Language Integrated Query_) é o nome de um conjunto de tecnologias com base na integração de 
recursos de consulta diretamente na linguagem C#. 

**Linq** habilita os desenvolvedores a interagir com qualquer tipo de dados, como objetos, bancos de dados e XML, 
diretamente a partir do código.

<note>
	Apesar de ser uma tecnologia desenvolvida para a linguagem C#, <code>Linq</code> 
	também pode ser utilizada no <b>IronPython</b>.
</note>

Esse, inlcusive, é um dos principais motivos pelos quais adotamos o IronPython para o desenvolvimento das rotinas 
para os nossos clientes e também para o nosso curso.

Falamos sobre isso no tópico [](CPython-x-IronPython.md).

Vamos perceber que usar **Linq** no IronPython é uma forma muito mais eficiente de trabalhar com coleções de dados do que
usar somente as funções nativas do Python.

## Principais Métodos

`Linq` possui muitos métodos, mas no nosso dia-a-dia de programação para a API do Revit, 
esses são os que mais utilizaremos:

**[](Where.md)** 
: Filtra uma sequência de valores com base em um predicado.

**[](Select.md)**
: Projeta cada elemento de uma sequência em um novo formulário.

**[](OrderBy.md)**
: Classifica os elementos de uma sequência em ordem crescente.

**[](FirstOrDefault.md)**
: Retorna o primeiro elemento de uma sequência ou `None` se o elemento não for encontrado.

**[](ToDictionary.md)**
: Cria um dicionário a partir de uma sequência.

<warning>
	<p>Todos os métodos acima esperam que passemos uma <b>função</b> como argumento.</p>
	<p>Eles utilizam essa função para realizar a operação desejada.</p>
</warning>

<note>
	<p>Essa função é chamada de <b>lambda</b> e é uma forma de escrever funções anônimas em Python.</p>
	<p>
		Em palavras mais simples, <i><b>é um jeito mais resumido de escrever uma função</b></i>, 
		sem precisar usar a sintaxe convencional, onde temos que escolher um nome para ela.
	</p>
</note>

```python
# Função convencional
def double(n):
    return 2 * n

print(double(7)) # 14
```

```python
# Função lambda
double = lambda n: 2 * n

print(double(7)) # 14
```