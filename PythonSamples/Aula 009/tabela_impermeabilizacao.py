# by onBIM Technology
# www.onbim.net
# file name: ./PythonSamples/Aula 009/tabela_impermeabilizacao.py

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

def GetElementNameById(elementId):
    element = doc.GetElement(elementId)
    return element.Name

def GroupByParameter(elementsAtMainKey):
    # Agrupar os elementos que estão na chave, por parâmetro
    elements_grouped_by_param = \
        elementsAtMainKey \
            .GroupBy(lambda element: GetElementCode(element)) \
            .ToDictionary(
            lambda group: group.Key,
            lambda group: group
        )
    
    # Substituindo os elements da chave principal    
    return elements_grouped_by_param

# FUNCTIONS
# END<<<<<

# INPUTS AND VARIABLES DECLARATIONS
# BEGIN>>>>>

doc = DocumentManager.Instance.CurrentDBDocument

file_path_to_export = IN[0]

result = []

# INPUTS AND VARIABLES DECLARATIONS
# END<<<<<

# MAIN CODE
# BEGIN>>>>>

try:
    errorReport = None
    
    """
    >>>> Coleta de paredes e pisos <<<<
    """
    
    # Listas de categorias a filtrar
    catsToFilter_as_python_list = [
        BuiltInCategory.OST_Floors,
        BuiltInCategory.OST_Walls,
    ]
    
    # Converter lista python para SystemList (.NET)
    catsToFilter = SystemList[BuiltInCategory](catsToFilter_as_python_list)

    # Cria o filtro de multi categoria
    multiCatFilter = ElementMulticategoryFilter(catsToFilter)
    
    # Coletar elementos usando ElementMulticategoryFilter
    floors_and_walls = \
        FilteredElementCollector(doc) \
            .WhereElementIsNotElementType() \
            .WherePasses(multiCatFilter) \
            .Where(lambda element: not isinstance(element, FamilyInstance)) \
    
    """
    >>>> Agrupar por nível <<<<
    """
    
    groups_by_level = \
        floors_and_walls \
        .GroupBy(lambda element: element.LevelId) \
        .ToDictionary(
            lambda group: GetElementNameById(group.Key),
            lambda group: group
        )
    
    """
    >>>> Sub-agrupar por parâmetro <<<<
    """
    
    elements_by_level_thenby_parameter = dict()
    
    for levelName in groups_by_level.Keys:
        elementsAtLevel = groups_by_level[levelName]
        
        elements_by_level_thenby_parameter[levelName] = GroupByParameter(elementsAtLevel)
    
    result = elements_by_level_thenby_parameter
    
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