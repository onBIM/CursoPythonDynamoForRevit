# by onBIM Technology
# www.onbim.net
# file name: ./Aula 004/truss.py

import clr
import traceback

# Import Dynamo Library Nodes - Geometry
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript import Geometry as DynamoGeometry

def ToList(obj):
    if not isinstance(obj, list):
        return [obj]
    
    return obj

def ValidateInteger(number, mustBePositive=False):
    if not isinstance(number, int):
        raise ValueError("n precisa ser um número inteiro")
        
    if mustBePositive and number < 0:
        raise ValueError("n precisa ser positivo")

def GeraListaDeParametros(n):
    ValidateInteger(n, True)
    
    if n == 0 or n == 1:
        return 0
    
    i = 0
    divisor = 1 / (n - 1)
    
    pars = []
    while i < n:
        pars.append(i * divisor)
        i = i + 1
    
    return pars

def GeraPontosNoBanzo(curva, nPontos):
    ValidateInteger(nPontos, True)
    
    if nPontos < 2:
        raise ValueError("O número de pontos precisa ser maior que 1")
    
    # Obtém os parâmetros
    parameters = GeraListaDeParametros(nPontos)
    
    # Retorna os pontos
    return [
        DynamoGeometry.Curve.PointAtParameter(curva,p)
        for p in parameters
    ]

def CriaOsMontantes(startPoints, endPoints):
    # TODO: criar função isso
    if len(startPoints) != len(endPoints):
        raise ValueError("As duas listas têm que ter o mesmo comprimento")
    
    return [
        DynamoGeometry.Line.ByStartPointEndPoint(start, end)
        for start, end in zip(startPoints, endPoints)
    ]

def CriaAsDiagonais(startPoints, endPoints):
    # TODO: criar função isso
    if len(startPoints) != len(endPoints):
        raise ValueError("As duas listas têm que ter o mesmo comprimento")
    
    # obtém start points das diagonais
    
    # sintaxe do slice
    # start : end : step
    # Observção: o end vai até o seu valor -1
    
    diagStartPoints = startPoints[:-1]
    
    diagEndPoints = endPoints[1:]
    
    return [
        DynamoGeometry.Line.ByStartPointEndPoint(start, end)
        for start, end in zip(diagStartPoints, diagEndPoints)
    ]

def CriaTrelica(banzoSuperior, hTruss, nMontantes):
    # Obtém o banzo inferior
    zAxis = DynamoGeometry.Vector.ZAxis()
    zAxisReverse = DynamoGeometry.Vector.Reverse(zAxis)
    
    banzoInferior = DynamoGeometry.Geometry.Translate(
        banzoSuperior,
        zAxisReverse,
        hTruss
    )
    
    # Obtém pontos do Banzo Superior
    pontosBanzoSup = GeraPontosNoBanzo(banzoSuperior, nMontantes)
    pontosBanzoInf = GeraPontosNoBanzo(banzoInferior, nMontantes)
    
    # Obtém os Montantes
    montantes = CriaOsMontantes(pontosBanzoSup, pontosBanzoInf)
    
    # Obtém as Diagonais
    diagonais = CriaAsDiagonais(pontosBanzoSup, pontosBanzoInf)
    
    return {
        "Banzo Superior" : banzoSuperior,
        "Banzo Inferior" : banzoInferior,
        "Pontos Banzo Sup" : pontosBanzoSup,
        "Pontos Banzo Inf" : pontosBanzoInf,
        "Montantes" : montantes,
        "Diagonais" : diagonais
    }

listaDeBanzos = ToList(IN[0])
altura_trelica = IN[1] # Altura da treliça
qtde_montantes = IN[2] # Número de montantes

# Variável de output
result = []

try:
    errorReport = None
    
    result = [
        CriaTrelica(banzo, altura_trelica, qtde_montantes)
        for banzo in listaDeBanzos
    ]
    
except Exception as e:
    # if error occurs anywhere in the process catch it
    errorReport = traceback.format_exc()

# Assign your output to the OUT variable
if errorReport is None:
    OUT = result
else:
    OUT = errorReport