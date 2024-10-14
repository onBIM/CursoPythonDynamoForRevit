class Pessoa:
    def __init__(self, nome):
        self.Nome = nome # Cria um novo atributo: Nome


class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        """
        Inicialize uma instância do Aluno.
        
        Args:
            nome (str): Nome do aluno.
            matricula (str): Número de matrícula do aluno.
        """
        super().__init__(nome) # Chame o método __init__ da classe pai
        
        self.Matricula = matricula  # Cria um novo atributo: Matricula


# Now you can create an instance of Aluno
student = Aluno("John Doe", "123456")
print(student.Nome)  # Output: John Doe
print(student.Matricula)  # Output: 123456