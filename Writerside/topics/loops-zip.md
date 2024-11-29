# zip

## Definição

A função `zip` pega um número variável de iteráveis e retorna um iterador de tuplas. 
Cada tupla contém os elementos na mesma posição dos iteráveis fornecidos.

O seu comportamento é similar ao do Node `Transpose` do Dynamo. Veja imagens abaixo 👇

### Node Transpose
![loops-zip-list-tranpose.png](loops-zip-list-tranpose.png) {width="600"}

### Função zip no Python
![loops-zip-on-python.png](loops-zip-on-python.png) {width="600"}

## Sintaxe

```python
zip(iteravel1, iteravel2, ...)
```

## Exemplo

```python
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado = zip(lista1, lista2)
print(list(resultado))  # Saída: [(1, 'a'), (2, 'b'), (3, 'c')]
```

<procedure title="Cuidados ao usar zip">
    <step>
        <p>
            <b>Tamanhos diferentes:</b> se os iteráveis passados para <code>zip</code> tiverem tamanhos diferentes, 
            o iterador resultante terá o mesmo tamanho do iterável mais curto. 
            Isso pode levar à perda de dados dos iteráveis mais longos.
        </p>
        <code-block lang="Python">
            # Exemplo onde um iterável é mais curto
            lista1 = [1, 2]
            lista2 = ['a', 'b', 'c']
            resultado = zip(lista1, lista2)
            print(list(resultado))  # Saída: [(1, 'a'), (2, 'b')]
        </code-block>
    </step>
    <step>
        <p>
            <b>Descompactação usando <code>zip(*iteravel_zip)</code></b>: Para descompactar iteráveis que 
            foram combinados usando <code>zip</code>, você pode usar a sintaxe <code>zip(*iteravel_zip)</code>.
        </p>
        <code-block lang="Python">
            # Exemplo de descompactação
            lista1 = [1, 2, 3]
            lista2 = ['a', 'b', 'c']
            combinado = list(zip(lista1, lista2))
            lista1_descompactada, lista2_descompactada = zip(*combinado)
            print(list(lista1_descompactada))  # Saída: [1, 2, 3]
            print(list(lista2_descompactada))  # Saída: ['a', 'b', 'c']
        </code-block>
    </step>
    <step>
        <p>
            <b>Iterabilidade:</b> <code>zip</code> retorna um iterador, não uma lista. Isso significa que você precisa 
            convertê-lo para uma lista se precisar acessar os dados várias vezes.
        </p>
        <code-block lang="Python">
            # Exemplo de aceitar um iterador de zip
            lista1 = [1, 2, 3]
            lista2 = ['a', 'b', 'c']
            resultado = zip(lista1, lista2)
            print(next(resultado))  # Saída: (1, 'a')
            print(next(resultado))  # Saída: (2, 'b')
        </code-block>
        <note>
            Note que após iterar até o final, os dados não podem ser reusados.
        </note>
    </step>
</procedure>

Com esses cuidados em mente, `zip` é uma ferramenta poderosa e flexível para combinar dados de múltiplos iteráveis de
maneira elegante.

## Exercícios

### Exercício 1
Calcular a soma de elementos emparelhados.

Crie duas listas de números com os valores `[10, 20, 30]` e `[1, 2, 3]`.

Use `zip` para emparelhar os elementos
correspondentes e, em seguida, calcule a soma de cada par. Imprima a lista de somas.

```python
# Listas de entrada
lista1 = [10, 20, 30]
lista2 = [1, 2, 3]

# Calculando a soma dos pares
somas = [a + b for a, b in zip(lista1, lista2)]

# Imprimindo o resultado
print(somas)  # Saída: [11, 22, 33]
```
