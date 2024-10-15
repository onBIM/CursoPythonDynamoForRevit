# Geometria do Dynamo no Python

## Descrição

Podemos utilizar a biblioteca de geometria do Dynamo no Node Python Script para fazermos
operações geométricas conforme as nossas necessidades.

```python
import clr

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript import Geometry as DynamoGeometry
```

Adiciona referência para os nodes de Geometria do Dynamo.

![dyn_geo_import.png](../../Aula%20001/01%20-%20Python%20dentro%20do%20Dynamo/images/dyn_geo_import.png)

# Exercício

![img.png](img.png)

Fazer uma treliça paramétrica.

INPUTS:

1. A curva que representa o banzo superior.
2. A altura da treliça.
3. O número de montantes.

OUTPUT:
1. Curvas dos banzos.
2. Linhas dos montantes
3. Linhas das Diagonais
