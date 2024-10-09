# Tipos de dados: string (str)

## Operações básicas de string

Strings são pedaços de texto. Elas podem ser definidas por qualquer coisa entre aspas(" " ou ' '):

```python
umastring = "Olá, Mundo!"
```

#### len

Retorna o tamanho da string



```python
print len(umastring)


```

#### index

Retorna o index do caractere na string

```python
print umastring.index("o")
print umastring.index("O")
```

#### count

Conta as ocorrências de um caractere no string

```python
print umastring.count("l")
```

#### slice

"parte" a string

```python
print umastring[3:7]
```

#### upper / lower

Muda a capitalização ("_case"_) da string para maiúscula ou minúscula, respectivamente.

```python
print umastring.upper()
print umastring.lower()
```

#### startswith / endwith

Indica se uma string começa / termina com a outra string passada como argumento

```python
print umastring.startswith("Olá")
print umastring.endswith("asdfasdfasdf")
```

#### split

Divide a string com base no caractere passado como argumento.

```python
umaspalavras = umastring.split(" ")
```