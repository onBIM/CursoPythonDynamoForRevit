# Orientação a objetos no Python

## Classes

Classes são a forma de organizar e criar objetos em Python. Elas são definidas pela palavra-chave `class` seguida 
do nome da classe e dois pontos. O corpo da classe é definido por indentação.

```python
class Pessoa:
    pass
```

> A palavra-chave `pass` é usada em Python para indicar que não há nada a ser feito. 
> Ela é usada quando a sintaxe requer um bloco de código, mas você não deseja executar nenhuma instrução.

### Objetos

Um objeto é uma instância de uma classe. Quando você cria um objeto, você está criando uma instância dessa classe.

```python
pessoa = Pessoa()
```

Neste exemplo, `pessoa` é um objeto da classe `Pessoa`.

### Métodos

Métodos são funções que pertencem a uma classe. Eles são definidos da mesma forma que funções, 
mas são definidos em uma classe.

```python
class Pessoa:
    def saudacao(self):
        print("Olá!")
```

> O primeiro argumento de um método de uma classe é sempre `self`. Ele é uma **referência ao objeto** que está chamando o 
> método.

### Construtor

O método `__init__` é um método especial chamado quando um objeto é criado. Ele é usado para inicializar o objeto.

```python
class Pessoa:
    def __init__(self, nome):
        self.Nome = nome
```

### Atributos

Atributos são variáveis que pertencem a um objeto. Eles são definidos dentro do método `__init__`.

```python
class Pessoa:
    def __init__(self, nome):
        self.Nome = nome
```

> Para acessar um atributo de um objeto, você usa a notação de ponto.

```python
pessoa = Pessoa("João")

print(pessoa.Nome)  # Isso imprimirá "João"
```

### Herança

Herança é a capacidade de criar uma nova classe que herda atributos e métodos de uma classe existente.

```python
class Pessoa:
    def __init__(self, nome):
        self.Nome = nome  # Cria um novo atributo: Nome


class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)  # Chame o método __init__ da classe pai
        
        self.Matricula = matricula  # Cria um novo atributo: Matricula


# Criando uma instância da classe Aluno
student = Aluno("John Doe", "123456")

print(student.Nome)  # Output: John Doe
print(student.Matricula)  # Output: 123456
```

Neste exemplo, a classe `Aluno` herda da classe `Pessoa`.

### Polimorfismo

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

fazer_barululho(gato)  # Isso imprimirá "Miau!"
fazer_barululho(cachorro)  # Isso imprimirá "Au au!"
```

Neste exemplo, `fazer_barulho` é uma função que aceita um argumento `animal` e chama o método `falar` desse animal.

> Em Python, o polimorfismo é implementado por meio de **duck typing**.

#### Duck Typing

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

### Encapsulamento

Encapsulamento é a capacidade de esconder a implementação de uma classe dos usuários da classe.

> Em Python, não há modificadores de acesso como em outras linguagens de programação.

```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo
```