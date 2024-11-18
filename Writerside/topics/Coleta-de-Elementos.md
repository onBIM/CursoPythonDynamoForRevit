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
        <p>A primeira coisa que precisamos fazer é configurar o nosso node Python Script para usar o IronPython como engine.</p>
        <p>Na nossa <b>Aula 001</b>, mostramos como fazer isso no tópico <a href="CPython-x-IronPython.md"/>.</p>
    </step>
    <step>
        <p>Agora é preciso importar todas as referências da API do Revit para podermos usá-las no nosso código.</p>
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
        <p>Agora precisamos criar uma instância da classe <code>FilteredElementCollector</code></p>
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
</procedure>

A primeira coisa que precisamos fazer é configurar o nosso node Python Script para usar o IronPython como engine.

Na nossa **Aula 001**, mostramos como fazer isso no tópico [CPython x IronPython](Aula-001.md#cpython-vs-ironpython).
