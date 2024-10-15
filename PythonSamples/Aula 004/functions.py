def ValidateInteger(number, mustBePositive=False):
    if not isinstance(number, int):
        raise ValueError("n precisa ser um número inteiro")
    
    if mustBePositive and number < 0:
        raise ValueError("n precisa ser positivo")

ValidateInteger(3.5)
