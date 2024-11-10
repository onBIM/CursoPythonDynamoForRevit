# Espécies de Famílias na API do Revit

Tem mais alguns conceitos sobre a API do Revit que são fundamentais antes de começarmos a programar. Esses conceitos são sobre as famílias no Revit.

Vamos entender melhor sobre isso.

Vimos no [tópico anterior](Conceitos-Basicos.md) que a hierarquia dos elementos no Revit é a seguinte:

🟨 _Category_ > 🟥 _Family_ > 🟩 _Type_ > 🟪 _Instances_

Bem, as famílias por sua vez são divididas em três espécies: 

> * **System** - Famílias de sistema. Exemplos: _Wall_, _Floor_, _Ceiling_.
> * **Loadable** - Famílias carregáveis. Exemplos: _Door_, _Window_, _Furniture_. 
> * **Model-in-place** - As famílias "modeladas no local" são espécies de famílias modeladas diretamente no projeto e que serão usadas apenas naquele projeto.
> 
{style="note"}

A API do Revit trata essas espécies de famílias de forma diferente. Veja na tabela abaixo:

|                    | _**Type**_   | _**Instance**_                                    |
|--------------------|--------------|---------------------------------------------------|
| **System**         | ElementType  | Classes próprias. Ex.: _Wall_, _Floor_, _Ceiling_ |
| **Loadable**       | FamilySymbol | FamilyInstance                                    |
| **Model-in-place** | FamilySymbol | FamilyInstance                                    |       

## Element Type

> A classe [ElementType](https://www.revitapidocs.com/2024/ffb18296-0448-559c-580c-7857cbcdc094.htm) ,
> representa **os tipos de famílias de sistema** no Revit.
> 
{style="note"}

![element-type-class.png](element-type-class.png)

Diz na documentação "_Base class for all types of elements in Autodesk Revit_" (Classe base para "todos" os tipos de elementos no Autodesk Revit).
Porém, como dissemos anteriormente, os _Element Types_ são apenas os tipos de famílias de sistema.

## Family Symbol

> A classe [FamilySymbol](https://www.revitapidocs.com/2024/a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm) 
> representa **os tipos de famílias carregáveis** e também os tipos de famílias Model-in-place no Revit.
> 
{style="note"}

![family-symbol-class.png](family-symbol-class.png)

Veja que na sessão **Remarks** da documentação diz em outras palavras o que falamos anteriormente em [Conceitos Básicos
da API do Revit](Conceitos-Basicos.md). Sendo que precisamos atentar que o _Remarks_ da imagem acima, refere-se a Famílias Carregáveis.

## Family Instance

> A classe [FamilyInstance](https://www.revitapidocs.com/2024/7b1b3b3b-0b3b-4b3b-8b3b-3b3b3b3b3b3b.htm) 
> representa **as instâncias de famílias carregáveis** e também as instâncias de famílias Model-in-place no Revit.
> 
{style="note"}

![family-instance-class.png](family-instance-class.png)

## Model-in-place

Perceba que:

> A API do Revit não tem classes específicas para os tipos e instâncias Model-in-place.
> 
{style="warning"}

Isso significa que as instâncias Model-in-place são tratadas da mesma forma que as instâncias de famílias carregáveis. 
De modo que não há um meio direto para identificar se uma instância é Model-in-place ou não.

Existem várias maneiras de contornar isso, porém as mais confiáveis são:

1. Para comparar se uma instância que deveria ser de **sistema** é Model-in-place ou não, use o método Python
`isinstance()` para comparar se a instância é da classe de sistema que você espera.
```python
if isinstance(suspect_wall, Wall):
    # É uma parede de sistema
else:
    # É uma parede Model-in-place
```

2. Para comparar se uma instância que deveria ser **carregável** é Model-in-place ou não, use diretamente as propriedades
      fornecidas pela API do Revit.
```python
if not suspect_door.Symbol.Family.IsInPlace:
    # É uma instância de família carregável
else:
    # É uma instância Model-in-place
```
* A propriedade `Symbol` retorna o tipo (`FamilySymbol`) da instância.
* A propriedade `Family`, por sua vez, retorna a família correspondente ao tipo da instância.

> Lembre-se da [Hierarquia dos elementos no Revit](Conceitos-Basicos.md#hierarquia-dos-elementos-no-revit) para entender melhor.

![is-in-place-property.png](is-in-place-property.png)

## Famílias no Dynamo do Revit

> A biblioteca do Dynamo tem **nomenclaturas diferentes** da API do Revit.
> 
{style="warning"}

Isso torna tudo um pouco mais confuso, mas vamos tentar simplificar nas tabelas abaixo.

### _Types_

O Dynamo chama os tipos de famílias da seguinte forma:

|                    | API do Revit | Dynamo         |
|--------------------|--------------|----------------|
| **System**         | ElementType  | ElementType    |
| **Loadable**       | FamilySymbol | **FamilyType** |
| **Model-in-place** | FamilySymbol | **FamilyType** |

### _Instances_

> A biblioteca do Dynamo não faz distinção entre instâncias de famílias de Sistema, Carregáveis e Model-in-place. 
> Ela chama todas de **Element**.
> 
{style="warning"}

### Exemplos da biblioteca do Dynamo

#### All Elements of Category

![all-elements-of-category.png](all-elements-of-category.png)

Este é um _Node_ que **retorna todas as instâncias que estão na categoria selecionada**.

Isso significa que ele retorna todas as instâncias de famílias de sistema, carregáveis e Model-in-place, 
sem fazer qualquer distinção.

> Veremos que usando a API do Revit existem meios diferentes para coletar instâncias de famílias de sistema e carregáveis.
> 
{style="note"}

#### All Elements of Family Type

![dynamo-revit-selection-node.png](dynamo-revit-selection-node.png)

Se fôssemos traduzir o nome do _Node_ da imagem acima👆 diretamente do inglês para o português, seria:

"Todos os elementos de um tipo de família".

Porém, com nosso entendimento sobre a API do Revit e Dynamo, a tradução mais precisa seria:

> "Todas as instâncias de um tipo de família carregável ou Model-in-place".
