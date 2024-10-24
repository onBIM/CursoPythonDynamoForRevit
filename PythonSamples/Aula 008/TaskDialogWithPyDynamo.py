# by onBIM Technology
# www.onbim.net
# file name: ./PythonSamples/Aula 008/TaskDialogWithPyDynamo.py

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

# Import Dynamo Library Nodes - Core
clr.AddReference('DSCoreNodes')
from DSCore import List as DynamoList

# Import Dynamo Library Nodes - Core
clr.AddReference('DSCoreNodes')
from DSCore import Color as DynamoColor

# Import Dynamo Geometry Color
# https://forum.dynamobim.com/t/geometrycolor-bygeometrycolor-inside-python/52724
clr.AddReference('GeometryColor')
from Modifiers import GeometryColor as DynamoGeometryColorize

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

# Import Revit User Interface API
clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import *

# Import Revit IFC API
# https://forum.dynamobim.com/t/ifcexportutils/4833/7?u=ricardo_freitas
clr.AddReference('RevitAPIIFC')
from Autodesk.Revit.DB.IFC import *

# Import Dynamo Services
clr.AddReference('DynamoServices')
from Dynamo import Events as DynamoEvents

# Active Dynamo Workspace Path
workspaceFullPath = DynamoEvents.ExecutionEvents.ActiveSession.CurrentWorkspacePath
workspacePath = '\\'.join(workspaceFullPath.split('\\')[0:-1])

import sys
pydynamoPath = r"D:\OneDrive\onBIM\Eventos\Curso Python for Dynamo 2024\CursoPythonDynamoForRevit\PythonSamples\Aula 008\pydynamo"
sys.path.append(pydynamoPath)
import pydynamo as pyd

# REFERENCES AND IMPORTS
# END<<<<<

# FUNCTIONS
# BEGIN>>>>>

# <<< Your classes and functions here >>>

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
    
    collectors = pyd.Collectors(doc)
    
    # Levels é uma System List por que Linq sempre retorna coleções do .NET
    levels = \
        collectors \
            .GetDocumentLevels() \
            .OrderBy(lambda level: level.Name) \
            .ToList()
    
    # Essa lista aqui é do Python porque estamos usando List Comprehension para criá-la
    levelsNames = [
        level.Name
        for level in levels
    ]
    
    tdResult = pyd.RevitTaskDialog(
        _Title="TaskDialog Curso Python",
        _MainInstruction="Exibe os níveis do documento",
        _MainContent="Os níveis do documento aberto são:\n\n" + pyd.ListToString(levelsNames, "\n"),
        _MainIcon=TaskDialogIcon.TaskDialogIconInformation,
        _CommonButtons=TaskDialogCommonButtons.Yes | TaskDialogCommonButtons.No
    )
    
    if tdResult == TaskDialogResult.CommandLink1:
        pyd.RevitTaskDialog(_MainInstruction="Email enviado")
        
    elif tdResult == TaskDialogResult.Yes:
        pyd.RevitTaskDialog(_MainInstruction="Você clicou em sim")
    
    result = tdResult

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