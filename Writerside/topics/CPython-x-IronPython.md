# CPython x IronPython

## Qual diferença entre o CPython e o IronPython ?

O CPython é a implementação padrão da linguagem Python, enquanto o IronPython é uma implementação alternativa
desenvolvida para rodar na plataforma .NET.

Em outras palavras isso significa que para usarmos os recursos da API do Revit o mais recomendado é o IronPython,
pois ele é capaz de acessar as bibliotecas .NET diretamente.

| Característica            | CPython                                  | IronPython                                    |
|---------------------------|------------------------------------------|-----------------------------------------------|
| Plataforma                | Independente de plataforma               | Plataforma .NET                               |
| Implementação             | Implementação padrão da linguagem Python | Implementação alternativa                     |
| Integração com .NET       | Não possui integração direta             | Acesso direto às bibliotecas do .NET          |
| Performance               | Geralmente mais performático             | Pode ser mais lento dependendo do uso do .NET |
| Suporte a Extensões C     | Sim                                      | Não                                           |
| Popularidade              | Mais popular e amplamente utilizado      | Menos popular em comparação ao CPython        |
| Ferramentas e Bibliotecas | Ampla variedade disponível               | Menor variedade, focado em .NET               |

### **A recomendação principal é:**

Não precisa acessar a API do Revit? Use CPython.
Se sim, use IronPython.

**Numa mesma rotina de Dynamo você pode ter Nodes Python Script que usam CPython e IronPython.**

## Como escolher a engine Python no Dynamo? {id="escolher-engine-python"}

![cpython_vs_ironpython.png](cpython_vs_ironpython.png) {style="block"}

- Clique com o botão direito no nó Python Script, selecione `Python Engine Version` e escolha a engine desejada.

ou alternativamente:

- Dentro do Editor Python, clique na caixa _drop-down_ e escolha a engine desejada.