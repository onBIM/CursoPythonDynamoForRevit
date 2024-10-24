# Diz para o Python onde o arquivo do módulo está

import sys

# caminho da pasta onde está o módulo
module_dir_path = "D:\OneDrive\onBIM\Eventos\Curso Python for Dynamo 2024\CursoPythonDynamoForRevit\PythonSamples\Aula 008\python_course_module"

sys.path.append(module_dir_path)

# Importa o módulo
import python_course_module as pyc

soma = pyc.Soma(3,5)

print(soma)