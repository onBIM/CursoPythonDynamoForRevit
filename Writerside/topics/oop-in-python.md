# Orientação a objetos no Python

## Classes

Classes são a forma de organizar e criar objetos em Python. É como se fossem um molde para criar objetos.

Fazendo uma analogia com um jogo [RPG](https://bit.ly/3CmAkcL), 
as classes seriam como as fichas de personagens, onde são definidas as suas características e habilidades.

As classes são definidas pela palavra-chave (_keyword_) `class`, seguida
do nome da classe e dois pontos. O corpo da classe é definido por indentação.

```python
class Mago:
    # corpo da classe
```

## Objetos

Um objeto é uma instância de uma classe. Quando você cria um objeto, você está criando uma instância dessa classe.

Novamente fazendo a analogia com RPG, o objeto seria então o personagem em si, criado a partir da ficha.

> É muito comum as pessoas fazerem confusão entre o que é uma classe e o que é um objeto. Mas agora você já sabe a diferença.
> 
{style="note"}

### Atributos

Atributos são variáveis que pertencem a um objeto. 

Usando nosso exemplo do RGP, os atributos então seriam **as características do personagem** como nome, idade, raça, 
etc.

> **Os atributos precisam ser definidos dentro do método** `__init__`, que é o **construtor** da classe. Falaremos mais sobre
> ele adiante.
> 
{style="warning"}

> Os atributos também podem ser chamados de **propriedades**.
> 
{style="note"}

### Métodos

Métodos são funções que pertencem a uma classe. Eles são definidos da mesma forma que funções,
porém dentro da classe.

No nosso exemplo do RPG, os métodos seriam as **ações que o personagem pode realizar** como atacar, defender, lançar.

```python
class Mago:
    def atacar(self):
        print("Ataque mágico!")

    def defender(self):
        print("Escudo mágico!")

    def lancar(self):
        print("Magia de fogo!")
```

> É obrigatório que o primeiro argumento de um método de uma classe seja sempre `self`. 
> 
{style="warning"}

O argumento `self` é uma **referência ao objeto** que o está chamando.

### Construtor

O método `__init__` é um método especial chamado quando um objeto é criado. Ele é usado para inicializar o objeto.

```python
class Mago:
    def __init__(self, nome, idade, raca):
        self.Nome = nome
        self.Idade = idade
        self.Raca = raca
```

Neste exemplo, `mago` é um objeto/instância da classe `Mago`. É o nosso personagem propriamente dito.

**Classe completa, com atributos e métodos:**
    
```python
class Mago:
    def __init__(self, nome, idade, raca):
        self.Nome = nome
        self.Idade = idade
        self.Raca = raca

    def atacar(self):
        print("Ataque mágico!")

    def defender(self):
        print("Escudo mágico!")

    def lancar(self):
        print("Magia de fogo!")
```

### Criando Objetos

Para criar um objeto, você chama a classe como se fosse uma função, passando os argumentos necessários definidos no
[construtor](#construtor).

```python
mago = Mago("Gandalf", 1000, "Istari")
```

### Acessando Atributos

Para acessar um atributo de um objeto, você usa a notação de ponto.

```python
nome_do_mago = mago.Nome

print(nome_do_mago)  # Isso imprimirá "Gandalf"
```

### Acessando Métodos

Para acessar um método de um objeto, você também usa a notação de ponto, porém com os parênteses.

Os métodos são funções. Portanto, seguem todas as regras de funções. Falamos delas [aqui](functions-in-python.md).

```python
mago.atacar()  # Isso imprimirá "Ataque mágico!"
```

## Herança

Herança é a capacidade de criar uma nova classe que herda atributos e métodos de uma classe existente.

Talvez essa seja a parte mais importante da orientação a objetos. A herança permite que você reutilize o código de uma
classe existente e evite a duplicação de código.

```python
class Pessoa:
    def __init__(self, nome):
        self.Nome = nome  # Cria um novo atributo: Nome


class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)  # Chame o método __init__ da classe mãe
        
        self.Matricula = matricula  # Cria um novo atributo: Matricula


# Criando uma instância da classe Aluno
student = Aluno("John Doe", "123456")

print(student.Nome)  # Output: John Doe
print(student.Matricula)  # Output: 123456
```

Neste exemplo, a classe `Aluno` herda da classe `Pessoa`.

> Na API do Revit temos muitos exemplos de herança. Por exemplo, a classe `Element` é a classe base para todos os 
> elementos do Revit. 
> 
{style="note"}

Por exempo, a classe `Wall` herda de `Element`, logo, herda todos seus os atributos e métodos.

![revit-api-wall-inheritance.png](revit-api-wall-inheritance.png)

![wall-inhereted-property](wall-inhereted-property.png)

## Polimorfismo

Polimorfismo é a capacidade de uma classe de se comportar como outra classe.

```python
class Gato:
    def falar(self):
        print("Miau!")

class Cachorro:
    def falar(self):
        print("Au au!")

def fazer_barulho(animal):
    animal.falar()

gato = Gato()
cachorro = Cachorro()

fazer_barulho(gato)  # Isso imprimirá "Miau!"
fazer_barulho(cachorro)  # Isso imprimirá "Au au!"
```

Neste exemplo, `fazer_barulho` é uma função que aceita um argumento `animal` e chama o método `falar` desse animal.

> Em Python o polimorfismo é implementado por meio de **duck typing**. Logo, não há um polimorfismo explícito como em
> outras linguagens de programação.
>
{style="warning"}

### Duck Typing

Duck typing é um conceito em programação que vem da frase "Se parece com um pato, nada como um pato e grasna como um
pato, então provavelmente é um pato". Em termos de programação, significa que a tipagem de uma variável é determinada
por suas operações e comportamento (métodos e propriedades) ao invés de sua classe ser derivada de uma hierarquia
específica.

Em Python, o duck typing é implementado permitindo que qualquer objeto que suporte determinada operação (método ou
atributo) seja utilizado naquele contexto, independentemente da classe a qual ele pertence.

```python
class Pato:
    def grasnar(self):
        print("Quack!")

class Pessoa:
    def grasnar(self):
        print("Eu sou uma pessoa, não um pato!")

def fazer_grasnar(objeto):
    objeto.grasnar()

pato = Pato()
pessoa = Pessoa()

fazer_grasnar(pato)    # Isso imprimirá "Quack!"
fazer_grasnar(pessoa)  # Isso imprimirá "Eu sou uma pessoa, não um pato!"
```

Neste exemplo, a função `fazer_grasnar` aceita qualquer objeto que tem um método `grasnar`. Não importa se `objeto` é um
`Pato`, uma `Pessoa` ou qualquer outra classe, desde que o método `grasnar` exista e possa ser chamado.

## Encapsulamento

Encapsulamento é a capacidade de esconder a implementação de uma classe dos usuários da classe.

> Em Python não há modificadores de acesso como em outras linguagens de programação. Portanto, por padrão, **todos os
> atributos e métodos de uma classe são públicos.**
>
{style="warning"}

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, quantia):
        self.saldo += quantia
    
    def sacar(self, quantia):
        if quantia <= self.saldo:
            self.saldo -= quantia
        else:
            print("Saldo insuficiente")

# Exemplo de uso:
conta = ContaBancaria("Alice", 1000)

# Acessando e modificando diretamente os atributos públicos
print(conta.saldo)  # Output: 1000
conta.saldo = 500
print(conta.saldo)  # Output: 500  (Modificado diretamente)

# Chamando métodos publicamente
conta.depositar(200)
print(conta.saldo)  # Output: 700

conta.sacar(100)
print(conta.saldo)  # Output: 600
```