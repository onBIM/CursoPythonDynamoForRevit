# by onBIM Technology
# www.onbim.net
# file name: ./Aula 006/FilteringByUserParameter.py

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
from System import Guid

# Import Linq
clr.ImportExtensions(System.Linq)

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

def GetParameterValue(param):
    if param is None and not isinstance(param, Parameter):
        return None
    
    storageType = param.StorageType
    
    if storageType == StorageType.Integer:
        return param.AsInteger()
        
    if storageType == StorageType.Double:
        return param.AsDouble()
    
    if storageType == StorageType.String:
        return param.AsString()
    
    if storageType == StorageType.ElementId:
        return param.AsElementId()
    
    raise Exception("Storage Type inválido")

# FUNCTIONS
# END<<<<<

# INPUTS AND VARIABLES DECLARATIONS
# BEGIN>>>>>

doc = DocumentManager.Instance.CurrentDBDocument

paramName = IN[0]

result = []

# INPUTS AND VARIABLES DECLARATIONS
# END<<<<<

# MAIN CODE
# BEGIN>>>>>

try:
    errorReport = None
    
    # Obtendo parâmetro usando API do Revit
    
    shared_parameter_guid = "a15e54db-8129-421a-8a5f-a504d17b67a3"
    
    guid = Guid.Parse(shared_parameter_guid)
    
    drywalls = \
        FilteredElementCollector(doc) \
        .OfClass(Wall) \
        .WhereElementIsNotElementType() \
        .Where(
            lambda wall:
            wall.WallType.get_Parameter(guid).AsInteger() == 1
        ) \
        .Select(lambda wall: wall.ToDSType(True))
    
    result = drywalls
    
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