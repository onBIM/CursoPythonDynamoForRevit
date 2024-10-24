# by onBIM Technology
# www.onbim.net
# file name: ./PythonSamples/Aula 008/room_data.py

# REFERENCES AND IMPORTS
# BEGIN>>>>>

import clr
import System
import math

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

class RoomData:
    def __init__(self, rvtRoom):
        self.Room = rvtRoom
        self.Id = rvtRoom.Id.IntegerValue
        self.IdAsString = str(self.Id)
        self.Name = rvtRoom.get_Parameter(BuiltInParameter.ROOM_NAME).AsString()
        self.Number = rvtRoom.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()
        self.FullName = self.Name + "-" + self.Number
        
        level = doc.GetElement(rvtRoom.LevelId)
        
        self.Level = level.ToDSType(True)

    def GetFinishes(self, includeLinkedElements=False, subFaceType=None):
        """
        Gets Rooms Finishes
         SubFaceType enum
         
         Bottom	
         A horizontal face at the bottom of the room, 
         as defined by the room's level and base offset, 
         or a face of the room that is bounded below by a room-bounding element.
    
         Top
         A horizontal top face of the room as defined by the room's level and height, 
         or a face of the room that is bounded above by a room-bounding element.
    
         Side	
         Any face which does not meet the criteria to be Top or Bottom.
        """
        # =================================================================
        # Get Room Finishes
        # =================================================================
        
        calculator = SpatialElementGeometryCalculator(doc)
        calculatorResults = calculator.CalculateSpatialElementGeometry(self.Room)
        roomSolid = calculatorResults.GetGeometry()
        finishes = []
        for face in roomSolid.Faces:
            # Retorna face vazia se não encontrar um elemento delimitador do Room.
            # Por exemplo um Room sem forro
            boundaryFaces = calculatorResults.GetBoundaryFaceInfo(face)
            if boundaryFaces != []:
                for bface in boundaryFaces:
                    faceType = bface.SubfaceType
                    
                    if (subFaceType is not None) and (faceType != subFaceType):
                        continue
                    
                    hostId = bface.SpatialBoundaryElement.HostElementId
                    hostDoc = doc
                    
                    hostFromLink = True if hostId.IntegerValue == -1 else False
                    
                    if includeLinkedElements and hostFromLink:
                        # Get host Id from link
                        linkedElementId = bface.SpatialBoundaryElement.LinkedElementId
                        hostId = linkedElementId
                        
                        # Get host linked document
                        linkInstanceId = bface.SpatialBoundaryElement.LinkInstanceId
                        linkedDocument = doc.GetElement(linkInstanceId).GetLinkDocument()
                        hostDoc = linkedDocument
                    
                    hostElement = hostDoc.GetElement(hostId)
                    
                    if hostElement is not None:
                        hostElementType = hostDoc.GetElement(hostElement.GetTypeId())
                        finishes.append(hostElement)
        
        return finishes.Select(lambda f: f.ToDSType(True))       
        
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
    
    rvtRooms = \
        FilteredElementCollector(doc) \
            .OfCategory(BuiltInCategory.OST_Rooms) \
            .WhereElementIsNotElementType() \
            .ToElements()
    
    result = \
        rvtRooms \
            .Select(lambda r: RoomData(r)) \
            .Where(lambda roomData: "M" in roomData.Name) \

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