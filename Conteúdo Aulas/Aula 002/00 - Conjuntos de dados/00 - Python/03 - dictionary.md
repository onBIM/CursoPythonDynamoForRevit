# Coleções de dados em Python

## Dicionários (dict)

### Definição

Um **dictionary** em Python é uma coleção de pares chave-valor.

Ele é mutável, o que significa que você pode alterar seu conteúdo após a criação.

Os dicionários são úteis para armazenar dados que precisam ser acessados por uma chave única.

Os dicionários são uma estrutura de dados poderosa e flexível em Python, permitindo o armazenamento e a manipulação eficiente de dados.

> **No Dynamo os dicionários só podem ter _keys_ do tipo `str` (_string_)**

### Exemplo de criação de um dictionary

```python
meu_dicionario = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}
```

### Principais métodos e propriedades

#### Acessar valores

* Você pode acessar um valor usando sua chave.

```python
nome = meu_dicionario["nome"]
```

#### Adicionar ou atualizar itens

* Para adicionar ou atualizar um item, basta atribuir um valor a uma chave.

```python
meu_dicionario["idade"] = 31
```

#### Remover itens

* Use `del` ou o método `pop()` para remover um item.

```python
del meu_dicionario["cidade"]
idade = meu_dicionario.pop("idade")
```

#### Obter todas as chaves

* Use o método `keys()` para obter uma lista de todas as chaves.

```python
chaves = meu_dicionario.keys()
```

#### Obter todos os valores

* Use o método `values()` para obter uma lista de todos os valores.

```python
valores = meu_dicionario.values()
```

#### Obter todos os pares chave-valor

* Use o método `items()` para obter uma lista de tuplas com pares chave-valor.

```python
itens = meu_dicionario.items()
```

#### Verificar se uma chave existe

* Use o operador `in` para verificar se uma chave está no dicionário.

```python
existe = "nome" in meu_dicionario
```
