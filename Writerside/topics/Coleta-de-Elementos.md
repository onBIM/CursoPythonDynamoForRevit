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

<procedure title="Usando o FilteredElementCollector" id="using-filtered-element-collector">
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
        <p>Por outro lado, se quisermos uma lista de <code>ElementId</code>, utilizamos o método <code>ToElementIds()</code>:</p>
        <code-block lang="Python">
            walls_ids = collector.OfCategory(BuiltInCategory.OST_Walls).ToElementIds()
        </code-block>
    </step>
</procedure>

