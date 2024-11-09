# Geometria do Dynamo no Python

Podemos utilizar a biblioteca de geometria do Dynamo no Node Python Script para fazermos
operações geométricas.

Veja como importar a biblioteca de geometria do Dynamo no Python:

```python
import clr

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript import Geometry as DynamoGeometry
```

![dyn_geo_import.png](dyn_geo_import.png)

Agora podemos utilizar as funções de geometria do Dynamo no Python.

```python
import clr

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript import Geometry as DynamoGeometry

# obtém os valores das coordenadas à partir dos inputs 
# do node Python Script no Dynamo
x = IN[0]
y = IN[1]
z = IN[2]

# Criando um ponto
ponto = DynamoGeometry.Point.ByCoordinates(x, y, z)

# Output do node Python Script no Dynamo
OUT = ponto
```

![point-with-python](point-with-python.png)

Dessa forma, podemos usar todos os recursos de geometria do Dynamo no Python.

> Somente as geometrias que você atribuir na variável `OUT` serão exibidas no Dynamo.
> 
{style="note"}

Isso é uma grande vantagem, pois significa que as geometrias utilizadas internamente no código Python não serão 
exibidas no Dynamo, o que trará granhos de performace para a sua rotina.

Por outo lado é um ponto de atenção para o desenvolvedor, pois já que as geometrias não são exibidas no Dynamo,
é preciso abstrair mais o raciocínio para fazer o que você deseja. E também pode trazer dificuldades para debugar.

> **As principais recomendações são**:
>
> 1. Evite códigos grandes demais em um único node Python Script no Dynamo.
> 2. Divida o código em funções.
> 3. Faça funções pequenas e com um único propósito.
> 4. Utilize comentários para explicar o que o código faz.
> 5. Utilize variáveis com nomes significativos.
> 6. Utilize a função `print()` para debugar o código se necessário.
>
{style="note"}

## Exercício 1

Fazer uma treliça paramétrica.

**INPUTS:**

1. A curva que representa o banzo superior.
2. A altura da treliça.
3. O número de montantes.

**OUTPUT:**

1. Curvas dos banzos.
2. Linhas dos montantes
3. Linhas das Diagonais

> **Dica** 💡
>
> Use a imagem abaixo como referência

![truss](truss.png)

### Resultado {id="resultado-exercicio-1"}

Ao final do exercício você deve ter algo parecido com a imagem abaixo:

![truss-in-dynamo.png](truss-in-dynamo.png)

Baixe a rotina aqui 👉 <resource src="truss.dyn"/>

## Exercício 2

Expandir o exercício anterior para funcionar em uma coberta completa.

> **Dica** 💡 
> 
> Use a família da supercície de coberta para fazer a treliça.
> 
> Baixe a família da coberta aqui 👉 <resource src="Surface.rfa"/>

> Modelada no Revit 2024. Portanto, só abre nessa versão ou superior.
> 
{style="warning"}

### Resultado {id="resultado-exercicio-2"}

Ao final do exercício você deve ter algo parecido com a imagem abaixo:

![organic-roof-trusses.png](organic-roof-trusses.png)

> A visualização colorida e transparente da coberta não é obrigatória. Foi mostrada dessa forma
> para facilitar a visualização da treliça.
> 
{style="note"}

Baixe a rotina aqui 👉 <resource src="Coberta-Organica.dyn"/>