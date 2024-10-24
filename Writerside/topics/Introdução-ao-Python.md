# Introdução ao Python

## O que é Python?

Python é uma linguagem de programação de alto nível, interpretada e de propósito geral. Criada por Guido van Rossum e
lançada em 1991, sua filosofia de design enfatiza a legibilidade do código, utilizando uma sintaxe que permite aos
programadores expressar conceitos em menos linhas de código em comparação com outras linguagens de programação, como C++
ou Java.

Python é dinâmicamente tipada, suportando múltiplos paradigmas de programação, incluindo programação procedural,
orientada a objetos e funcional. Ela possui uma ampla biblioteca padrão e uma abundância de bibliotecas de
terceiros, o que a torna extremamente versátil para diferentes tipos de projetos, desde desenvolvimento web até ciência
de dados e inteligência artificial.

## Principais Características do Python

- **Legibilidade e simplicidade:** A sintaxe do Python é clara e intuitiva, o que torna a linguagem acessível tanto para
  iniciantes quanto para programadores experientes.
- **Dinamicamente tipada:** Em Python, você não precisa declarar o tipo das variáveis, pois ele é inferido
  automaticamente pelo interpretador.
- **Interpretada:** O código Python é executado linha a linha, o que facilita a depuração e o teste de pequenos trechos
  de código.
- **Versatilidade:** Python é adequado para uma ampla gama de aplicações, desde web development e scripts de automação
  até ciência de dados e aprendizado de máquina.
- **Paradigmas de programação múltiplos:** Suporta programação procedural, orientada a objetos e funcional.
- **Biblioteca padrão extensa:** Inclui módulos para tarefas comuns como manipulação de strings, comunicação de rede,
  serviços web e interfaces gráficas.
- **Comunidade ativa:** Python possui uma grande comunidade de desenvolvedores e uma vasta quantidade de recursos,
  incluindo tutoriais, documentações e bibliotecas de terceiros.

## Python como uma Linguagem Interpretada

Python é uma linguagem interpretada, o que significa que o **código é executado linha a linha pelo interpretador**, em
vez de ser compilado previamente em código de máquina antes da execução.

Isso oferece várias vantagens, tais como uma
depuração mais fácil e uma maior flexibilidade durante o desenvolvimento.

### Exemplo de Código Interpretado em Python

Aqui está um exemplo simples de execução de código Python em um ambiente interativo:

```python
>>> a = 5
>>> b = 10
>>> c = a + b
>>> print(c)
15
```

Neste exemplo, cada linha de código é executada assim que é digitada. O Python calcula a soma de `a` e `b` e armazena o
resultado em `c`. Em seguida, imprime o valor de `c`.

### Vantagens de uma Linguagem Interpretada

1. **Depuração em Tempo Real:** Você pode testar e depurar o código linha por linha sem a necessidade de recompilar o
   programa inteiro.
2. **Flexibilidade:** Alterações no código podem ser feitas e testadas rapidamente, tornando o desenvolvimento mais
   eficiente.
3. **Facilidade no Desenvolvimento:** Ideal para scripts e prototipagem rápida, onde a velocidade de desenvolvimento é
   crucial.

### Comparação com Linguagens Compiladas

Para entender a diferença entre uma linguagem interpretada como Python e uma linguagem compilada, vejamos um exemplo
de código em C# (uma linguagem compilada):

```c#
using System;
class Program
{
    static void Main()
    {
        int a = 5;
        int b = 10;
        int c = a + b;
        Console.WriteLine(c);
    }
}
```

Neste exemplo, o código C# é compilado em código de máquina antes de ser executado. Ao contrário de Python, onde cada
linha pode ser executada diretamente no interpretador, o código C# precisa ser compilado primeiro por um compilador
antes
de ser executado. O compilador verifica o código fonte para erros e cria um arquivo executável.