# by onBIM Technology
# www.onbim.net
# file name: ./resources/python/collecting-chairs.py

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

# INPUTS AND VARIABLES DECLARATIONS
# BEGIN>>>>>

doc = DocumentManager.Instance.CurrentDBDocument

result = []

# INPUTS AND VARIABLES DECLARATIONS
# END<<<<<

# MAIN CODE
# BEGIN>>>>>

try:
    errorReport = None
    
    # Já que as cadeiras estão na categoria Furniture,
    # vamos criar um filtro de categoria para Furniture.
    catFilter = ElementCategoryFilter(BuiltInCategory.OST_Furniture)
    
    # Obtendo o piso a partir da seleção do usuário no Dynamo
    floor = UnwrapElement(IN[0])
    
    bbox = floor.get_BoundingBox(None)
    outline = Outline(bbox.Min, bbox.Max)
    
    # Criando um filtro de interseção de BoundingBox
    bboxIntersectsFilter = BoundingBoxIntersectsFilter(outline)
    
    # Criando um filtro lógico AND
    filtersToCombine = SystemList[ElementFilter]([
        catFilter,
        bboxIntersectsFilter
    ])
    
    logicalAndFilter = LogicalAndFilter(filtersToCombine)
    
    furnitures_and_caseworks_on_floor = \
        FilteredElementCollector(doc) \
        .WherePasses(logicalAndFilter) \
        .Where(lambda element: "Chair" in element.Name) \
        .ToList()
    
    result = furnitures_and_caseworks_on_floor

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