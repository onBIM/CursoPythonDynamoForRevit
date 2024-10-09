# Números em Python

## int

Números inteiros

## float

Números decimais

## Operações Matemáticas Básicas

*   Soma "+"
*   Subtração "-"
*   Multiplicação "\*"
*   Divisão "/"
*   Divisão inteira "//"
*   Resto "%"

## Funções Matemáticas

Usando diretamente o módulo **Python**

```python
import math
```

Usando a Lib do **Dynamo**

```python
# Import Dynamo Library Nodes - Core
import clr
clr.AddReference('DSCoreNodes')
from DSCore import Math as DynamoMath
```

Usando a Lib do **System** (Somente no IronPython)

```python
# Import System Libraries
import clr
clr.AddReference("System.Core")
from System import Math as SystemMath
```