# Select

## Definição

O método `Select` é utilizado para **aplicar** uma função a cada elemento da coleção.

> Apesar do nome `Select` dar a entender que estamos "selecionando" algo, na verdade, 
> estamos **aplicando** uma função a cada elemento da coleção.
> 
> Portanto, não confunda o método `Select` com o método `Where`.
> 
{style="warning"}

## Exemplo 1

Vamos supor que tenhamos uma lista de números e queremos obter o quadrado de cada um deles.

Usando o método `Select` do **Linq** podemos fazer isso de forma muito mais eficiente e simples, 
sem a necessidade de usar um laço `for`.

```python
import clr

# Adiciona a referência para o System.Core
clr.AddReference("System.Core")

# Importa os métodos de extensão do LINQ.
import System
clr.ImportExtensions(System.Linq)

# input pela porta do node Python Script no Dynamo
numeros = IN[0]

quadrados = numeros.Select(lambda n: n ** 2)

OUT = quadrados
```

![linq-select-squares.png](linq-select-squares.png) {thumbnail="true" width="700"}

Perceba que o código acima é muito mais simples e direto do que se tivéssemos que usar um laço `for` para percorrer a lista de números.

> Outra grande vantagem de **Linq** é que podemos encadear os métodos, facilitando ainda mais 
> o processo de lidar com coleções.
> 
{style="note"}

Vamos supor que no exemplo anterior, queiramos obter somente os quadrados pares. 
Para isso, podemos encadear o método `Where` logo após o `Select`.

```python
import clr

# Adiciona a referência para o System.Core
clr.AddReference("System.Core")

# Importa os métodos de extensão do LINQ.
import System
clr.ImportExtensions(System.Linq)

# input pela porta do node Python Script no Dynamo
numeros = IN[0]

quadrados = \
	numeros \
	.Select(lambda n: n ** 2) \
	.Where(lambda n: n % 2 == 0)

OUT = quadrados
```

![linq-select-even-squares.png](linq-select-even-squares.png)  {thumbnail="true" width="700"}

## Exercício

Faça um código que obtenha o **_Level_** de todas as paredes da família _Basic Wall_ do modelo.

> Utilize o método `Select` para obter o **_Level_** de cada parede.
> 
{style="tip"}

<chapter title="Solução">

</chapter>

