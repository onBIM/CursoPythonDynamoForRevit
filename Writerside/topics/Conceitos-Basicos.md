# Conceitos Básicos da API do Revit

Para programar para o Revit é necessário entender alguns conceitos básicos da API do Revit.

Geralmente esses conceitos não são mostrados em cursos convencionais de Revit, ou são mostrados de forma superficial.

No nosso curso, vamos abordar esses conceitos de forma mais aprofundada, 
para que você possa entender como a API do Revit funciona e como você pode utilizá-la para automatizar tarefas no Revit.

As nossas principais referências são: 

* Livro [Mastering Autodesk Revit 2020](https://amzn.to/3NZIj1Y), de Simon 
Whitbread.
* [Dynamo Primer](https://primer.dynamobim.org/).
* Documentação oficial da [API do Revit](https://www.revitapidocs.com/2024/).

## Hierarquia dos Elementos no Revit

No Revit, os elementos são organizados em uma hierarquia, como em uma biblioteca, 
onde nós temos sessões, prateleiras, livros e páginas.

No Revit temos a seguinte hierarquia:

🟨 _Category_ > 🟥 _Family_ > 🟩 _Type_ > 🟪 _Instances_

Veja a imagem abaixo

![revit-elements-hierarchy.png](revit-elements-hierarchy.png) {id="revit-elements-hierarchy.png"}

### Category

A categoria é o nível mais alto da hierarquia. Ela agrupa elementos que possuem características semelhantes e que 
representam objetos do mundo real.

Exemplo: _Walls_, _Floors_, _Ceilings_, _Doors_, _Windows_, _Furniture_, _Lighting Fixtures_, _Plumbing Fixtures_

> No Revit as categorias são **imutáveis**, ou seja, não é possível criar novas categorias ou alterar as existentes.
> 
{style="warning"}

Isso tem o propósito de manter a informação organizada e padronizada. Lembra como funcionam os _Layers_ do AutoCAD, na prática 
do dia-a-dia? 🤯

> Porém, é possível criar subcategorias, que são chamadas de _Subcategories_.
> 
{style="note"}

### Family

A família é um conjunto de elementos (_Types_) que compartilham características comuns. 

Por exemplo, na [imagem acima](#revit-elements-hierarchy.png), temos a família _Rectangular Column_ que possui 
os _Types_ **_450 x 600 mm_** e **_600 x 700 mm_**,

### Type

O tipo representa uma variação de uma família. No tipo estão definidas as propriedades que serão comuns entre as instâncias.

Por exemplo, na [imagem acima](#revit-elements-hierarchy.png), temos o _Type_ **_450 x 600 mm_** da família _Rectangular Column_.
Nele estão contidas as propriedades que são comuns a todas as instâncias desse tipo. Como a altura, a largura, o material, etc.

### Instance

Até o momento, todos os conceitos anteriores são "abstrações" que servem para organizar os elementos no Revit.

No caso da instância, ela é o **elemento "materializado" no projeto**. O elemento de um _Type_ específico de uma _Family_.

Veja o exemplo na imagem abaixo de como o Revit organiza os elementos dessa forma no _Project Browser_.

![elements-hierarchy-on-project-browser.png](elements-hierarchy-on-project-browser.png)

## Dados dos elementos

O segundo conceito mais importante sobre o Revit é:

> **No Revit os dados estão nos elementos.**
> 
{style="note"}

Pode até parecer óbvio demais, mas nem todos os softwares BIM funcionam dessa forma.

Quer ver exemplos?

* No AutoCAD, os dados, na maioria das vezes, estão em _Tags_. Desse modo a informação fica "desconectada" do elemento, apenas sendo reconhecida por um humano.
* No AECOsim, os dados podem estar em arquivos XML separados dos elementos. Veja alguns links sobre isso:
<a href="https://docs.bentley.com/LiveContent/web/AECOsim%20Building%20Designer%20Help-v5/en/GUID-ACA8D618-A87D-4AE4-FFE4-227E77130AF1.html?form=MG0AV3">Tagged Elements</a>
<a href="https://docs.bentley.com/LiveContent/web/AECOsim%20Building%20Designer%20Help-v5/en/GridSystemXMLImportExportDbox.html?form=MG0AV3">XML Import and Export Grid Systems</a>

Isso tem tantas implicações que é até difícil saber por onde começar. Mas talvez o ponto mais óbvio seja:

> Se você quiser obter informação de um elemento no Revit, você as encontrará no próprio elemento.
> 
{style="note"}

Mais uma vez, parece até óbvio demais, mas é muito comum em forums de Revit perguntas do tipo:

* "Como eu faço para obter informação da parede na tabela de quantitativos?"
* "Por que o Revit não funciona igual ao Excel e não me deixa criar uma coluna na tabela de quantitativos com a informação que eu quero?"

A resposta para essas perguntas é sempre a mesma: **"Porque no Revit os dados estão nos elementos"** e não nas tabelas.

Então se você quiser saber a altura de uma parede, você vai procurar na própria parede e não em uma tabela de quantitativos.

Mas daí então o que são as tabelas no Revit? 

A resposta é: **As tabelas são apenas uma forma de visualizar os dados que estão nos elementos.** Em outras palavras:

> **Cada linha de uma tabela de quantitativos é um elemento do Revit**. E cada coluna é uma propriedade desse elemento.
> 
{style="note"}

Vamos ver mais na frente e, na prática, que existem métodos na API do Revit destinados a isso.