# Tipos de dados: Booleano (bool)

## Definição no Python

Valores booleanos são dois objetos constantes **Falso** e **Verdadeiro**.
No contexto numérico eles se comportam como os inteiros 0 e 1, respectivamente.
A função de construção `bool()` pode ser usada para converter qualquer valor para um Boolean,
se o valor puder ser interpretado como um valor verdadeiro.

São escritos como `False` e `True`, respectivamente.

Servem para tomadas de decisão ou _toggle_ (chave liga/desliga) em Nodes Python Script do Dynamo.

## Na API do Revit

Servem principalmente para "ligar/desligar" funcionalidades.
Em fórmulas de parâmetros também servem para tomadas de decisão.
Parâmetros desse tipo são chamados **Yes/No** no Revit e podem assumir `null` (nulo) como um terceiro valor.

![Bool Sample in Revit](images/bool_sample_in_revit.png)

## Operadores de Comparação
| Operador | Descrição                                     |
|----------|-----------------------------------------------|
| \==      | compara se dois valores são iguais            |
| !=       | compara se dois valores são diferentes        |
| <        | compara se um valor é menor que o outro       |
| \>       | compara se um valor é maior que o outro       |
| <=       | compara se um valor é menor ou igual ao outro |
| \>=      | compara se um valor é maior ou igual ao outro |

## Operadores Lógicos
| Operador | Descrição                                         |
|----------|---------------------------------------------------|
| **and**  | operador lógico "E"                               |
| **or**   | operador lógico "OU"                              |
| **not**  | operador lógico "NÃO"                             |
| **in**   | determina se um objeto está dentro de uma coleção |

## Funções importantes
| Função           | Descrição                                     |
|------------------|-----------------------------------------------|
| **isinstance()** | determina se um objeto é do Tipo especificado |
| **hasattr()**    | verifica se um objeto possui uma propriedade  |

## Controle de fluxo com "if / elif / else"

### If

Já o `if` deve propor alguma coisa. É preciso escrever o IF e logo depois colocar a condição analisada. 
Então, em seguida, o bloco de comandos.

```python
if n % 2 == 0:
  print("Número par")
```

### Elif

O `elif` é uma estrutura intermediária dentro da seção if-else no python e deve vir como um complemento a ambos. 
Quando você já tem um IF e um ELSE, mas precisa de uma condição para especificar outra regra, pode usar o elif.

Caso algo não tenha ficado exatamente claro, não se preocupe: estudaremos em detalhes como se faz o código 
dessas estruturas em um tutorial prático.

```python
if not isinstance(n, int):
  print("Erro. Você precisa entrar um número inteiro")
elif n % 2 == 0:
  print("Número par")
else:
  print("Número ímpar") 
```

#### Else

O `else` surge depois do IF, em complemento lógico a ele.

Não é possível escrever um ELSE sem um IF antes.

O ELSE não requer um teste, uma comparação, pois ele executa algo caso a comparação do IF não passe.

Portanto, você só precisa declarar o ELSE e adicionar o bloco de comandos.

```python
if n % 2 == 0:
  print("Número par")
else:
  print("Número ímpar")
```
## Comparações múltiplas

O Python aceita comparações múltiplas. Veja o exemplo abaixo:

```python
idade = int(input("Digite sua idade: "))

if 18 <= idade < 70:
    print("Você pode receber o benefício")
else:
    print("Você não pode receber o benefício")
```
