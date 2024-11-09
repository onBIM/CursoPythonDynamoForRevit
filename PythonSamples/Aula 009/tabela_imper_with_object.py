# by onBIM Technology
# www.onbim.net
# file name: ./PythonSamples/Aula 009/tabela_imper_with_object.py

# REFERENCES AND IMPORTS
# BEGIN>>>>>

import clr
import System
import csv

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

# REFERENCES AND IMPORTS
# END<<<<<

# FUNCTIONS
# BEGIN>>>>>

class ImperElement:
    def __init__(self, element):
        self.Element = element
        self.Category = self.Element.Category.Name
        self.Level = self.GetLevelElement()
        self.Code = self.GetElementCode()
        self.Area = self.GetElementArea()
        self.Length = self.GetElementLength()
        
        # self.UnitConverter = UnitsConvertionTools()

    def GetLevelElement(self):
        levelId = self.Element.LevelId
        
        return doc.GetElement(levelId)
    
    def GetElementCode(self):
        # Obtendo Id do Type
        typeId = self.Element.GetTypeId()
        
        # Obtendo o Type do Element
        elementType = doc.GetElement(typeId)
        
        return elementType.LookupParameter(".TCM_Sistemas_Codigo").AsString()
    
    def GetElementArea(self):
        internalArea = self.Element.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED).AsDouble()
        
        return UnitsConvertionTools().InternalAreaToDisplayUnits(internalArea)
    
    def GetElementLength(self):
        if isinstance(self.Element, Floor):
            return 0
        
        if isinstance(self.Element, Wall):
            internalLength = self.Element.get_Parameter(BuiltInParameter.CURVE_ELEM_LENGTH).AsDouble()
            
            return UnitsConvertionTools().InternalLengthToDisplayUnits(internalLength)
        
        raise Exception("Não foi possível obter o comprimento do elemento. Elemento inválido")
    
    def Serialize(self):
        return [
            self.Category,
            self.Element.Id.Value,
            self.Element.Name,
            self.Level.Name,
            self.Code,
            self.Area,
            self.Length
        ]

class UnitsConvertionTools:
    def __init__(self, document=None):
        if document is not None:
            self.doc = document
        else:
            self.doc = DocumentManager.Instance.CurrentDBDocument
    
    class SpecTypes:
        Length = SpecTypeId.Length
        Area = SpecTypeId.Area
        Angle = SpecTypeId.Angle
    
    class UnitsTypes:
        Millimeters = UnitTypeId.Millimeters
        Centimeters = UnitTypeId.Centimeters
        Meters = UnitTypeId.Meters
        SquareCentimeters = UnitTypeId.SquareCentimeters
        SquareMeters = UnitTypeId.SquareMeters
    
    # Getting Display Units 
    def GetLengthDisplayUnits(self):
        formatOptions = self.doc.GetUnits().GetFormatOptions(self.SpecTypes.Length)
        
        return formatOptions.GetUnitTypeId()
    
    def GetAreaDisplayUnits(self):
        formatOptions = self.doc.GetUnits().GetFormatOptions(self.SpecTypes.Area)
        
        return formatOptions.GetUnitTypeId()
    
    def GetAngleDisplayUnits(self):
        formatOptions = self.doc.GetUnits().GetFormatOptions(self.SpecTypes.Angle)
        
        return formatOptions.GetUnitTypeId()
    
    # Conversions
    def InternalLengthToCM(self, x):
        return UnitUtils.ConvertFromInternalUnits(x, self.UnitsTypes.Centimeters)
    
    def InternalLengthToDisplayUnits(self, x):
        return UnitUtils.ConvertFromInternalUnits(x, self.GetLengthDisplayUnits())
    
    def InternalAreaToDisplayUnits(self, x):
        return UnitUtils.ConvertFromInternalUnits(x, self.GetAreaDisplayUnits())
    
    def InternalAreaToSquareMeters(self, x):
        return UnitUtils.ConvertFromInternalUnits(x, self.UnitsTypes.SquareMeters)
    
    def InternalAngleToDisplayUnits(self, x):
        return UnitUtils.ConvertFromInternalUnits(x, self.GetAngleDisplayUnits())
    
    def LengthDisplayUnitsToInternal(self, x):
        return UnitUtils.ConvertToInternalUnits(x, self.GetLengthDisplayUnits())
    
    def AreaDisplayUnitsToInternal(self, x):
        return UnitUtils.ConvertToInternalUnits(x, self.GetAreaDisplayUnits())
    
    def AngleDisplayUnitsToInternal(self, x):
        return UnitUtils.ConvertToInternalUnits(x, self.GetAngleDisplayUnits())
    
    def CMToInternalLength(self, x):
        return UnitUtils.ConvertToInternalUnits(x, self.UnitsTypes.Centimeters)
    
    def MToInternalLength(self, x):
        return UnitUtils.ConvertToInternalUnits(x, self.UnitsTypes.Meters)
    
    def SquareCMToInternalArea(self, x):
        return UnitUtils.ConvertToInternalUnits(x, self.UnitsTypes.SquareMeters)
    
    def SquareMToInternalArea(self, x):
        return UnitUtils.ConvertToInternalUnits(x, self.UnitsTypes.SquareMeters)
    
    def SquareCMToSquareM(self, x):
        return UnitUtils.Convert(x, self.UnitsTypes.SquareCentimeters, self.UnitsTypes.SquareMeters)
    
    def SquareMToSquareCM(self, x):
        return UnitUtils.Convert(x, self.UnitsTypes.SquareMeters, self.UnitsTypes.SquareCentimeters)
    
    def CMToDisplayUnits(self, x):
        return UnitUtils.Convert(x, self.UnitsTypes.Centimeters, self.GetLengthDisplayUnits())
    
    def DisplayUnitsToCM(self, x):
        return UnitUtils.Convert(x, self.GetLengthDisplayUnits(), self.UnitsTypes.Centimeters)
    
# FUNCTIONS
# END<<<<<

# INPUTS AND VARIABLES DECLARATIONS
# BEGIN>>>>>

doc = DocumentManager.Instance.CurrentDBDocument

file_path = IN[0]

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
    >>>> criando objetos de impermeabilização <<<<
    """
    imperElements = floors_and_walls.Select(lambda element: ImperElement(element))
    
    """
    >>>> exportando para csv <<<<
    """
    data = list(
        imperElements.Select(lambda imperEle: imperEle.Serialize()).ToList()
    )
    
    headers = [
       "Category",
       "Id",
       "Name",
       "LevelName",
       "Code",
       "Area",
       "Length"
    ]
    
    data.insert(0, headers)

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)
        
    result = data
    
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