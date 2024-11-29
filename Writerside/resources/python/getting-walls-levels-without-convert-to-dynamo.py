# by onBIM Technology
# www.onbim.net
# file name: ../resources/python/getting-walls-levels-without-convert-to-dynamo.py

# REFERENCES AND IMPORTS
# BEGIN>>>>>

import clr
import System

# <<< Python Modules >>>
# BEGIN

# Import traceback module from Iron Python
import traceback

# END

# Import System Libraries
clr.AddReference("System.Core")
from System.Collections.Generic import List as SystemList

# Import Linq
clr.ImportExtensions(System.Linq)

# Import Dynamo Library Nodes - Geometry
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript import Geometry as DynamoGeometry

# Import Dynamo Library Nodes - Revit
clr.AddReference("RevitNodes")
import Revit as RevitNodes

# Import ToDSType(bool) extension method
clr.ImportExtensions(RevitNodes.Elements)
clr.ImportExtensions(RevitNodes.GeometryConversion)

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import Revit API
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# REFERENCES AND IMPORTS
# END<<<<<

# FUNCTIONS
# BEGIN>>>>>

def GetElementById(document, elementId): 
    """
    Retorna um elemento de um documento usando o ID exclusivo do elemento.

    Esta função acessa o documento fornecido para localizar e retornar o
    elemento com o ID especificado. O ID deve ser exclusivo dentro do
    contexto do documento. Se o elemento for encontrado, ele retorna o elemento.
    A operação depende do método `GetElement` do documento.

    @param document: O Documento do qual o elemento deve ser 
        recuperado.
    @param elementId: O ID do elemento a ser 
        recuperado do documento.
    @return: O elemento obtido do documento que corresponde ao ID fornecido.
    """
    return document.GetElement(elementId)

# FUNCTIONS
# END<<<<<

# INPUTS AND VARIABLES DECLARATIONS
# BEGIN>>>>>

doc = DocumentManager.Instance.CurrentDBDocument

inputFromDynamo = IN[0]

result = []

# INPUTS AND VARIABLES DECLARATIONS
# END<<<<<

# MAIN CODE
# BEGIN>>>>>

try:
    errorReport = None
    
    basic_walls = \
        FilteredElementCollector(doc) \
        .OfClass(Wall) \
        .Where(
            lambda wall: 
            wall.WallType.Kind == WallKind.Basic
            and not wall.IsStackedWallMember
        )
    
    walls_levels = \
        basic_walls \
        .Select(lambda wall: GetElementById(doc, wall.LevelId))
    
    result = [
        basic_walls,
        walls_levels
    ]

except Exception as e:
    # if error occurs anywhere in the process catch it
    errorReport = traceback.format_exc()

# Assign your output to the OUT variable
if errorReport is None:
    OUT = result
else:
    OUT = errorReport
# MAIN CODE
# END<<<<<