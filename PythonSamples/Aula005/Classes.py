class Pessoa:
    def __init__(self, nome, cpf, estado):
        self.Name = nome
        self.CPF = cpf
        self.Estado = estado
        
class Aluno(Pessoa):
    def __init__(self, nome, cpf, estado, matricula):
        super().__init__(nome, cpf, estado)
        
        self.Matricula = matricula

ricardo = Pessoa("Ricardo", "123.456.789", "PE")
joao = Pessoa("João", "987.654.321", "SP")

joazinho = Aluno("Joãozinho", "000.000.000.000", "PE", "12345")

print(joazinho.CPF)