# Coleta de Elementos

Sabemos que na biblioteca padrão do Dynamo existem alguns nodes que nos ajudam a coletar elementos do Revit. 
Porém, muitas vezes esses nodes não são suficientes para o que precisamos.

Já que dispomos do Python, que por sua vez nos dá acesso direto a API do Revit, o mais recomendado é que usemos o Python para coletar elementos.

A ferramenta que usaremos para isso é o `FilteredElementCollector`.

## O que é o FilteredElementCollector

Segundo a documentação da API do Revit, 

> O [`FilteredElementCollector`](https://www.revitapidocs.com/2024/263cf06b-98be-6f91-c4da-fb47d01688f3.htm) é uma classe 
> usada para procurar, filtrar e [iterar](https://bit.ly/3OdTK6f) sobre um conjunto de elementos do Revit.
> 
{style="note"}

![filtered-element-collector-class.png](filtered-element-collector-class.png)

Ela é a melhor maneira de coletar elementos do Revit, pois é a mais eficiente e a que consome menos recursos do computador.

Os próprios nodes do Dynamo que coletam elementos usam o `FilteredElementCollector` por baixo dos panos.

## Como usar o FilteredElementCollector

O procedimento abaixo mostra como usar o `FilteredElementCollector` para coletar elementos do Revit.

Clique no ícone ➕ para expandir o procedimento.

<procedure title="Usando o FilteredElementCollector" id="using-filtered-element-collector" collapsible="true" default-state="collapsed">
    <step>
        <p>Configurar o nosso node Python Script para usar o IronPython como engine.</p>
        <p>Na nossa <b>Aula 001</b>, mostramos como fazer isso no tópico <a href="CPython-x-IronPython.md"/>.</p>
    </step>
    <step>
        <p>Importar todas as referências da API do Revit para podermos usá-las no nosso código.</p>
        <p>Veja o tópico <a href="Template-Python-onBIM.md"/> para ver como fazer isso.</p>
        <note>
            Lembre-se também de importar as referências de <b>Linq</b> e <b>System List</b>.
        </note>
        <p>
            Apesar de não utilizarmos elas incialmente, vai ser muito comum precisar depois. Então aproveita e já vai
            se acostumando a fazer isso.
        </p>
    </step>
    <step>
        <p>Criar uma instância da classe <code>FilteredElementCollector</code></p>
        <p>Para isso, usamos o seguinte código:</p>
        <code-block lang="python">
            collector = FilteredElementCollector(doc)
        </code-block>
        <p>Usando nosso template, como recomendado, ao final seu código deve ter algo parecido com isso:</p>
        <code-block lang="python" 
                    src="../resources/revit-api-imports.py" 
                    collapsible="true" 
                    collapsed-title="Código básico para usar API do Revit" 
                    default-state="collapsed"/>
    </step>
    <step>
        <p>Filtrando por Categoria ou pela Classe que representa a instância de família de sistema.</p>
        <p>
            Para isso, usamos o método 
            <a href="https://www.revitapidocs.com/2024/c3523c35-4a07-9723-3c28-de3cc47b2ad0.htm"><code>OfCategory()</code></a> 
            ou <a href="https://www.revitapidocs.com/2024/b0a5f22c-6951-c3af-cd29-1f28f574035d.htm"><code>OfClass()</code></a> 
            do <code>collector</code>, respectivamente.
        </p>
        <p>
            Por exemplo, se quisermos coletar todas as paredes do projeto usando o método <code>OfCategory()</code> 
            e armazenar na variável <code>walls</code>, teremos o seguinte código:
        </p>
        <code-block lang="python">
            walls = collector.OfCategory(BuiltInCategory.OST_Walls)
        </code-block>
        <warning>
            Note que usando o método <code>OfCategory()</code> todos os 
            elementos que pertencem à <code>BuiltInCategory.OST_Walls</code> serão coletados. Isso incluirá:
            <list>
                <li>As instâncias de paredes de sistema.</li>
                <li>
                    <p>
                        Os <b><i>Types</i></b> de paredes. Sim, eles também serão coletados, 
                        pois também fazem parte da categoria <code>Walls</code>.
                    </p>
                    <p>
                        Veja a imagem abaixo da inspeção de uma parede do modelo usando o 
                        <a href="https://github.com/jeremytammik/RevitLookup">Revit Lookup</a> 👇
                       <img src="wall-inspection.png" alt="Inpeção de parede com o Revit Lookup" style="block" border-effect="line"/>
                    </p>
                </li>
                <li>As instâncias de paredes <b><i>Model-in-place</i></b></li>
            </list>
        </warning>
        <p>
            Portanto, será necessário mais filtragens para obter os resultados que queremos, pois raramente iremos 
            querer todos os elementos da categoria sem qualquer filtragem.
        </p>
        <note>
            Para ver uma lista completa de todas as <code>BuiltInCategory</code> acesse 
            <a href="https://www.revitapidocs.com/2024/ba1c5b30-242f-5fdc-8ea9-ec3b61e6e722.htm">Revit API docs | BuiltInCategory</a>
        </note>
        <p>
            Por outro lado, se quisermos coletar todas as paredes do projeto usando o método <code>OfClass()</code> 
            e armazenar na variável <code>walls</code>, teremos o seguinte código:
        </p>
        <code-block lang="python">
            walls = collector.OfClass(Wall)
        </code-block>
        <note>
            Note que agora como estamos usando o método <code>OfClass()</code>, apenas as 
            <u>instâncias de paredes de <b>sistema</b></u> serão coletadas.
        </note>
        <tip>
            Lembre-se do tópico <a href="Conceitos-Sobre-Familias.md"/> desse curso.
        </tip>
    </step>
    <step>
        <p>Transformar o <code>FilteredElementCollector</code> em uma lista de <code>Element</code> ou de <code>ElementId</code>.</p>
        <p>
            O mais comum é utilizarmos o método 
            <a href="https://www.revitapidocs.com/2024/732b4a0d-62d8-b86d-120b-8ea3d9713b34.htm"><code>ToElements()</code></a>,
            que, como o próprio nome diz, transforma o <code>FilteredElementCollector</code> em uma lista de <code>Element</code>.
        </p>
        <code-block lang="Python">
            walls = collector.OfCategory(BuiltInCategory.OST_Walls).ToElements()
        </code-block>
        <img src="collect-walls.png" alt="Coletando paredes por categoria" style="block"/>
        <p>Por outro lado, se quisermos uma lista de <code>ElementId</code>, utilizamos o método <code>ToElementIds()</code>:</p>
        <code-block lang="Python">
            walls_ids = collector.OfCategory(BuiltInCategory.OST_Walls).ToElementIds()
        </code-block>
        <img src="collect-walls-ids.png" alt="Coletando ids por categoria" style="block"/>
    </step>
</procedure>

## Mais opções de filtragem com o FilteredElementCollector

Antes de coverter o `FilteredElementCollector` para lista podemos fazer muitas outras filtragens. 

Para isso utilizamos o método [`WherePasses()`](https://www.revitapidocs.com/2024/42d4eef3-55a1-2739-0ef8-6bc1d9fc2755.htm) 
do `FilteredElementCollector`.

Note que este método recebe um objeto do tipo [`ElementFilter`](https://www.revitapidocs.com/2024/b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm) como argumento.

![wherepasses-method.png](wherepasses-method.png)

O `ElementFilter` é uma classe base que possui três classes principais derivadas que caracterizam o "tipo" de filtro: 

Cada uma dessas classes por sua vez possui várias classes derivadas que representam os filtros específicos.
No nosso código utilizamos essas classes filhas para criar os filtros.

Veja a lista abaixo:

<procedure title="Tipos de filtro" collapsible="true" default-state="collapsed">
    <step>
        <p><a href="https://www.revitapidocs.com/2024/3b8d6b55-0cab-1810-1188-840800e5eaa2.htm"><code>ElementLogicalFilter</code></a></p>
        <p>Essa classe é utilizada para combinar vários filtros</p>
        <p>Classes derivadas:</p>
        <img src="element-logical-filter.png" alt="ElementLogicalFilter"/>
    </step>
    <step>
        <p><a href="https://www.revitapidocs.com/2024/ebc95d82-11fc-69f6-2df1-52331dd36443.htm"><code>ElementQuickFilter</code></a></p>
        <p>Essa classe é utilizada para filtrar elementos de forma rápida</p>
        <p>Classes derivadas:</p>
        <img src="element-quick-filter.png" alt="ElementQuickFilter"/>
        <p>As mais usadas são: <code>BoundingBoxIntersectsFilter</code> e <code>ElementMulticategoryFilter</code></p>
    </step>
    <step>
        <p><a href="https://www.revitapidocs.com/2024/e06b1e14-dd8d-8137-74ac-8ac4929eee85.htm"><code>ElementSlowFilter</code></a></p>
        <p>Essa classe é utilizada para filtrar elementos de forma mais lenta.</p>
        <warning>Cuidado. Esse filtro é bastante lento e consome bem mais memória, como pode ser visto na sessão <i>Remarks</i></warning>
        <p>Classes derivadas:</p>
        <img src="element-slow-filter.png" alt="ElementSlowFilter"/>
        <p>A mais usada é: <code>ElementIntersectsFilter</code></p>
    </step>
</procedure>

### Exemplos de uso do `WherePasses()`

A seguir, mostramos alguns exemplos de uso do método `WherePasses()`.

#### Usando um `ElementQuickFilter`

Vamos o usar o [`ElementMulticategoryFilter`](https://www.revitapidocs.com/2024/34f8d848-4440-e880-3277-4f90e5cf3072.htm)
para filtrar elementos de várias categorias.

Esse filtro possui várias formas de instanciá-lo, porém a mais comum é passando uma lista de `BuiltInCategory` como 
argumento.

![mult-cat-filter-constructors.png](mult-cat-filter-constructors.png)

```python
    # Criando uma System List de BuiltInCategory, 
    # pois o construtor do ElementMulticategoryFilter 
    # não aceita uma lista Python    
    cats = SystemList[BuiltInCategory]([
        BuiltInCategory.OST_Walls,
        BuiltInCategory.OST_Floors
    ])
    
    multCatFilter = ElementMulticategoryFilter(cats)
    
    walls_and_floors = \
        FilteredElementCollector(doc) \
        .WherePasses(multCatFilter) \
        .ToElements()
    
    result = walls_and_floors
```

<note>
    <p>Veja como foi necessário criar uma <code>List</code> do <code>System</code> para poder utilizar o construtor do filtro.</p>
    <p>Falamos disso no tópíco <a href="collections-system.md">Coleções | System</a></p>
</note>

<tip>
    <p>Perceba que para evitarmos linhas de código muito longas, que podem ser difíceis de ler, utilizamos a barra invertida `\`
    para quebrar a linha.</p>
    <p>Essa é forma que o Python permite quebrar uma linha de código em várias linhas, sem causar erros de sintaxe.</p>
</tip>

![collecting-walls-and-floors.png](collecting-walls-and-floors.png)

<note>
    <p>Note que foi necessário mudarmos a engine Python para <code>IronPython</code> para que o código acima funcionasse.</p>
    <p>Falamos sobre isso no tópico <a href="CPython-x-IronPython.md"></a></p>
</note>


