umastring = "Olá, Mundo cão, e f.. !"

print(umastring)

print("O número de caracteres é: ", len(umastring))

print("O index do caractere 'M' é: ", umastring.index("M"))

# Conta as ocorrências de um caractere no string
print("A quantidade de caracteres 'M' é: ", umastring.count("M"))

# slice
print(umastring[5:10])

# upper / lower
print(umastring.upper())
print(umastring.lower())

# split
print(umastring.split(", "))

# replace
print(umastring.replace("Mundo", "Python"))