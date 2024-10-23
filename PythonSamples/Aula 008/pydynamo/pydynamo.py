# -*- coding: utf-8 -*-
"""
pydynamo module created by onBIM Technology
https://www.onbim.net

file name: pydynamo.py

for encoding issues look at:
https://www.python.org/dev/peps/pep-0263/
"""
# REFERENCES AND IMPORTS
# BEGIN>>>>>


import clr, sys, System

# <<< Iron Python Modules >>>
# BEGIN

# Import traceback module from Iron Python
import traceback
import csv
from clr import StrongBox
import random as rnd

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
import clr
clr.AddReference('DynamoServices')
from Dynamo import Events as DynamoEvents

def HelloWorld():
    return 'Hello Python'

def ToList(item):
    """
    @param item: The input parameter which can be of any type.
    @return: Turns any item into a list. If the item is already a list, it returns the item itself.
    """
    return item if isinstance(item, list) else [item]

def flatten(listToFlatten):
    if len(listToFlatten) == 0:
        return listToFlatten
    if isinstance(listToFlatten[0], list):
        return flatten(listToFlatten[0]) + flatten(listToFlatten[1:])
    return listToFlatten[:1] + flatten(listToFlatten[1:])

def ListToString(mylist, separator):
    """
    type: list -> str
     Turns a list into string
    """
    return separator.join([str(item) for item in mylist])

def StringToList(mystring, separator):
    return mystring.split(separator)

def NumberToString(num, decimalsymbol="."):
    numStr = str(round(num, 1)).split(".")

    intStr = numStr[0]
    decimalStr = numStr[1]

    if intStr == "0" and decimalStr == "0":
        return ""
    elif intStr != "0" and decimalStr == "0":
        return intStr
    else:
        return "{0}.{1}".format(intStr, decimalStr)

def ReplaceItemFor(myList, itemToSearch, itemToReplace):
    """
    Replaces a item for a another given item
     by onBIM Technology
    """
    return [itemToReplace if i == itemToSearch else i for i in ToList(myList)]

def RevitTaskDialog(
    _Title="Default Title",
    _MainIcon=TaskDialogIcon.TaskDialogIconNone,
    _AllowCancellation=False,
    _MainInstruction=None,
    _MainContent=None,
    _FooterText=None,
    _ExpandedContent=None,
    _VerificationText=None,
    _CommonButtons=None,
    _DefaultButton=None,
    _EnableMarqueeProgressBar=False
    ):
    # adapted from:
    # https://spiderinnet.typepad.com/blog/2011/06/taskdialog-of-revit-api-1-a-comprehensive-taskdialog-example.html

    # ========================================================
    # Task Dialog stuff
    # ========================================================
    # Constructor
    td = TaskDialog(_Title)
    
    # << TaskDialogIcon Enumeration >>

    # TaskDialogIconNone	    No icon.
    # TaskDialogIconShield	    Shield icon.
    # TaskDialogIconInformation	Information icon.
    # TaskDialogIconError	    Error icon.
    # TaskDialogIconWarning	    Warning icon.
    td.MainIcon = _MainIcon

    # General properties
    td.Title = _Title
    td.TitleAutoPrefix = False # False para não aparecer o nome do comando 'Dynamo Script' no título
    td.AllowCancellation = _AllowCancellation

    # Message related stuffs
    td.MainInstruction = _MainInstruction
    td.MainContent = _MainContent
    td.FooterText = _FooterText
    td.ExpandedContent = _ExpandedContent

    # VerificationText stuff
    td.VerificationText = _VerificationText

    # ========================================================
    # Command link stuffs
    # ========================================================
    # td.AddCommandLink(TaskDialogCommandLinkId.CommandLink1, "This is 'CommandLink1'.")
    # td.AddCommandLink(TaskDialogCommandLinkId.CommandLink2, "This is 'CommandLink2'.")
    # td.AddCommandLink(TaskDialogCommandLinkId.CommandLink3, "This is 'CommandLink3'.")
    # td.AddCommandLink(TaskDialogCommandLinkId.CommandLink4, "This is 'CommandLink4'.")

    # ========================================================
    # Common button stuffs
    # ========================================================
    # << TaskDialogCommonButtons Enumeration >>
    
    # None	    No common button.
    # Ok	    OK button.
    # Yes	    Yes button.
    # No	    No button.
    # Cancel	Cancel button.
    # Retry	    Retry button.
    # Close	    Close button.
    
    # Example Code for Command Buttons
    # TaskDialogCommonButtons.Cancel |\
    # TaskDialogCommonButtons.Ok |\
    # TaskDialogCommonButtons.Close |\
    # TaskDialogCommonButtons.No |\
    # TaskDialogCommonButtons.Yes |\
    # TaskDialogCommonButtons.Retry |\
    # TaskDialogCommonButtons.None
    td.CommonButtons = _CommonButtons if _CommonButtons is not None else TaskDialogCommonButtons.Ok

    # << TaskDialogResult Enumeration >>

    # None	        Nothing is returned from the task dialog.
    # Ok	        The return value for TaskDialogCommonButtons.Ok.
    # Cancel	    The return value for TaskDialogCommonButtons.Cancel or the task dialog is cancelled by ESC, Alt+F4 or the X close button.
    # Retry	        The return value for TaskDialogCommonButtons.Retry.
    # Yes	        The return value for TaskDialogCommonButtons.Yes.
    # No	        The return value for TaskDialogCommonButtons.No.
    # Close	        The return value for TaskDialogCommonButtons.Close.
    # CommandLink1	The return value for CommandLink whose Id is TaskDialogCommmandLinkId.CommandLink1.
    # CommandLink2	The return value for CommandLink whose Id is TaskDialogCommmandLinkId.CommandLink2.
    # CommandLink3	The return value for CommandLink whose Id is TaskDialogCommmandLinkId.CommandLink3.
    # CommandLink4	The return value for CommandLink whose Id is TaskDialogCommmandLinkId.CommandLink4.
    
    # Progress Bar
    td.EnableMarqueeProgressBar = _EnableMarqueeProgressBar

    # Dialog showup stuffs
    tdResult = td.Show()

    return tdResult

def CheckDocument(inputdoc):
    if inputdoc == None:
        doc = DocumentManager.Instance.CurrentDBDocument
    elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.RevitLinkInstance":
        doc = inputdoc.GetLinkDocument()
    elif inputdoc.GetType().ToString() == "Autodesk.Revit.DB.Document":
        doc = inputdoc
    else: doc = None
    return doc

class PyDynamoVars:
    # Active Dynamo Workspace Path
    WorkspaceFullPath = DynamoEvents.ExecutionEvents.ActiveSession.CurrentWorkspacePath
    WorkspacePath = '\\'.join(WorkspaceFullPath.split('\\')[0:-1])

    Doc = DocumentManager.Instance.CurrentDBDocument
    UIapp = DocumentManager.Instance.CurrentUIApplication
    App = UIapp.Application
    UIdoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

    RevitVersionName = App.VersionName
    RevitVersionNumber = int(App.VersionNumber)

class ApplicationInfo:
    VersionName = PyDynamoVars.App.VersionName
    VersionNumber = int(PyDynamoVars.App.VersionNumber)
    UserName = PyDynamoVars.App.Username
    VersionBuild = PyDynamoVars.App.VersionBuild

class UnitsConvertionTools:
    def __init__(self, doc=None):
        if doc is not None:
            self.doc = doc
        else:
            self.doc = PyDynamoVars.Doc
    
    class SpecTypes:
        if PyDynamoVars.RevitVersionNumber < 2021:
            Length = UnitType.UT_Length
            Area = UnitType.UT_Area
            Angle = UnitType.UT_Angle
        else:
            Length = SpecTypeId.Length
            Area = SpecTypeId.Area
            Angle = SpecTypeId.Angle

    class UnitsTypes:
        if PyDynamoVars.RevitVersionNumber < 2021:
            Millimeters = DisplayUnitType.DUT_MILLIMETERS
            Centimeters = DisplayUnitType.DUT_CENTIMETERS
            Meters = DisplayUnitType.DUT_METERS
            SquareCentimeters = DisplayUnitType.DUT_SQUARE_CENTIMETERS
            SquareMeters = DisplayUnitType.DUT_SQUARE_METERS
        else:
            Millimeters = UnitTypeId.Millimeters
            Centimeters = UnitTypeId.Centimeters
            Meters = UnitTypeId.Meters
            SquareCentimeters = UnitTypeId.SquareCentimeters
            SquareMeters = UnitTypeId.SquareMeters

    # Getting Display Units 
    def GetLengthDisplayUnits(self):
        formatOptions = self.doc.GetUnits().GetFormatOptions(self.SpecTypes.Length)
        
        if PyDynamoVars.RevitVersionNumber < 2021:
            return formatOptions.DisplayUnits
        else:
            return formatOptions.GetUnitTypeId()

    def GetAreaDisplayUnits(self):
        formatOptions = self.doc.GetUnits().GetFormatOptions(self.SpecTypes.Area)

        if PyDynamoVars.RevitVersionNumber < 2021:
            return formatOptions.DisplayUnits
        else:
            return formatOptions.GetUnitTypeId()

    def GetAngleDisplayUnits(self):
        formatOptions = self.doc.GetUnits().GetFormatOptions(self.SpecTypes.Angle)

        if PyDynamoVars.RevitVersionNumber < 2021:
            return formatOptions.DisplayUnits
        else:
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

    def GetAllUnitsForgeTypeIds(self):
        """List all ForgeTypeIds

        Returns:
            [list(ForgeTypeId)]: List of all ForgeTypeIds
        """
        # Adapted from
        # https://github.com/jeremytammik/the_building_coder_samples/blob/master/BuildingCoder/BuildingCoder/Util.cs#L1306-L1367
        # fti.ToString(), 
        # fti.TypeId,
        # UnitUtils.GetTypeCatalogStringForUnit( fti ),
        # LabelUtils.GetLabelForUnit( fti );
           
        forgeTypeIds =\
            UnitUtils\
            .GetAllUnits()\
            .OrderBy(lambda x: UnitUtils.GetTypeCatalogStringForUnit(x))\

        return\
            forgeTypeIds,\
            [UnitUtils.GetTypeCatalogStringForUnit(fti) for fti in forgeTypeIds],\
            [fti.TypeId for fti in forgeTypeIds],\

class BoundingBoxData:
    def __init__(self, BoundingBox):
        self.OriginalBoundingBox = BoundingBox
        
        # Bounding box min and max points
        self.MinPoint = self.OriginalBoundingBox.MinPoint
        self.MaxPoint = self.OriginalBoundingBox.MaxPoint

        self.Cuboid = self.OriginalBoundingBox.ToCuboid()

        self.Edges = self.Cuboid.Edges.Select(lambda edge: edge.CurveGeometry)

        self.Faces = self.Cuboid.Faces.Select(lambda face: face.SurfaceGeometry()).ToList()

        # Bounding box all vertices as points
        self.Vertices = self.Cuboid.Vertices.Select(lambda vertice: vertice.PointGeometry).ToList()

        # Bounding box centroid
        self.Centroid = self.Cuboid.Centroid()

        # Centroid of Bottom Face
        self.CentroidOfBottomFace =\
            DynamoGeometry\
            .Point\
            .ByCoordinates(
                self.Centroid.X, 
                self.Centroid.Y, 
                self.MinPoint.Z
            )

        # Bounding Box context Coordinate System
        self.CoordinateSystem =\
            DynamoGeometry\
            .CoordinateSystem\
            .ByOrigin(self.MinPoint)
    
    def offset(self, offset):
        # Bounding box offset
        offVecMax = DynamoGeometry.Vector.ByCoordinates(offset, offset, offset)
        offVecMin = DynamoGeometry.Vector.Reverse(offVecMax)
        # offDist = offset*Math.Sqrt(3)
        offDist = offset**1/3

        minPoint = self.OriginalBoundingBox.MinPoint
        maxPoint = self.OriginalBoundingBox.MaxPoint
        
        newMin = minPoint.Translate(offVecMin, offDist)
        newMax = maxPoint.Translate(offVecMax, offDist)

        newBBox = DynamoGeometry.BoundingBox.ByCorners(newMin, newMax)

        return BoundingBoxData(newBBox)

class RoomData:
    def __init__(self, room):
        self.Room = room
        self.Id = str(room.Id.IntegerValue)
        self.Name = room.get_Parameter(BuiltInParameter.ROOM_NAME).AsString()
        self.Number = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()
        self.FullName = self.Name + "-" + self.Number

class RoomGeometryData:
    def __init__(self, room, calculator):
        self.Name = room.get_Parameter(BuiltInParameter.ROOM_NAME).AsString()
        self.Number = room.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()

        self.FullName = self.Name + "-" + self.Number
        
        calculatorResults = calculator.CalculateSpatialElementGeometry(room)
        self.Solid = calculatorResults.GetGeometry()

        self.Faces = self.Solid.Faces

class Collectors:
    def __init__(self, doc=None):
        self.doc = doc

        if doc is None:
            self.doc = PyDynamoVars.Doc
            
    def GetAllValidRooms(self):
        """
        Gets all valid Rooms from Document
        """
        validRooms =\
            FilteredElementCollector(self.doc)\
            .OfCategory(BuiltInCategory.OST_Rooms)\
            .WhereElementIsNotElementType()\
            .Where(lambda r:
                r.IsValidObject
                and r.Area > 0
                and r.get_BoundingBox(None) is not None)

        return list(validRooms)

    def GetAllInvalidRooms(self):
        """
        Gets all invalid Rooms from Document
        """
        invalidRooms =\
            FilteredElementCollector(self.doc)\
            .OfCategory(BuiltInCategory.OST_Rooms)\
            .WhereElementIsNotElementType()\
            .Where(lambda r:
                r.IsValidObject
                and r.Area == 0
                or r.get_BoundingBox(None) is None)

        return list(invalidRooms)
    
    def GetValidRoomsFromActiveDesignOption(self):
        """
        Gets all valid Rooms from Document from active Design option
        """
        activeDesignOptionId = DesignOption.GetActiveDesignOptionId(self.doc)

        designOptionFilter = ElementDesignOptionFilter(activeDesignOptionId)

        validRooms =\
            FilteredElementCollector(self.doc)\
            .OfCategory(BuiltInCategory.OST_Rooms)\
            .WhereElementIsNotElementType()\
            .WherePasses(designOptionFilter)\
            .Where(lambda r:
                r.IsValidObject
                and r.Area > 0
                and r.get_BoundingBox(None) is not None)

        return list(validRooms)

    def GetValidRoomsFromDesignOption(self, designOptionId):
        designOptionFilter = ElementDesignOptionFilter(designOptionId)

        validRooms =\
            FilteredElementCollector(self.doc)\
            .OfCategory(BuiltInCategory.OST_Rooms)\
            .WhereElementIsNotElementType()\
            .WherePasses(designOptionFilter)\
            .Where(lambda r:
                r.IsValidObject
                and r.Area > 0
                and r.get_BoundingBox(None) is not None)

        return list(validRooms)

    def GetDocumentLevels(self):
        """
        Gets all Levels from Document
        """
        levels =\
            FilteredElementCollector(self.doc)\
            .OfCategory(BuiltInCategory.OST_Levels)\
            .WhereElementIsNotElementType()\
            .Where(lambda x: x.IsValidObject)\

        return list(levels)

    def GetRoomFinishes(self, room, calculator, includeLinkedElements=False, subFaceType=None):
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
        calculatorResults = calculator.CalculateSpatialElementGeometry(room)
        roomSolid = calculatorResults.GetGeometry()
        finishes = []
        for face in roomSolid.Faces:
            # Retorna face vazia se não encontrar um elemento delimitador do Room
            # Por exemplo um Room sem forro
            boundaryFaces = calculatorResults.GetBoundaryFaceInfo(face)

            if boundaryFaces.Any():
                for bface in boundaryFaces:
                    faceType = bface.SubfaceType

                    if (subFaceType is not None) and (faceType != subFaceType):
                        continue
                    
                    hostId = bface.SpatialBoundaryElement.HostElementId
                    hostDoc = self.doc
                    
                    hostFromLink = True if hostId.IntegerValue == -1 else False

                    if includeLinkedElements and hostFromLink:
                        # Get host Id from link
                        linkedElementId = bface.SpatialBoundaryElement.LinkedElementId
                        hostId = linkedElementId
                        
                        # Get host linked document
                        linkInstanceId = bface.SpatialBoundaryElement.LinkInstanceId
                        linkedDocument = self.doc.GetElement(linkInstanceId).GetLinkDocument()
                        hostDoc = linkedDocument

                    hostElement = hostDoc.GetElement(hostId)

                    if hostElement is not None:
                        hostElementType = hostDoc.GetElement(hostElement.GetTypeId())
                        finishes.append(hostElement)

        return finishes

    def GetProjectParameters(self):
        """
        Get project parameteres data
         return: ParameterData[]
        """ 
        bindingsMap = self.doc.ParameterBindings

        iterator = bindingsMap.GetEnumerator()

        parameters = []
        while iterator.MoveNext():
            # get the parameter definition
            definition = iterator.Key
            
            # get element binding
            elementBinding = iterator.Current

            parameters.append(ProjectParameterData(definition=definition, elementBinding=elementBinding))

        return parameters

    def GettAllRoomSeparationLines(self):
        """
        Get all Room Separation Lines from Document
        """
        roomSeparationLines =\
            FilteredElementCollector(self.doc)\
            .OfCategory(BuiltInCategory.OST_RoomSeparationLines)\
            .WhereElementIsNotElementType()\
            .Where(lambda x: x.IsValidObject)

        return list(roomSeparationLines)

    def GetRoomSeparationLinesFromDesignOption(self, designOptionId):
        """
        Get all Room Separation Lines from Document from Design Option
        """
        designOptionFilter = ElementDesignOptionFilter(designOptionId)
        
        roomSeparationLines =\
            FilteredElementCollector(self.doc)\
            .OfCategory(BuiltInCategory.OST_RoomSeparationLines)\
            .WherePasses(designOptionFilter)\
            .WhereElementIsNotElementType()\
            .Where(lambda x: x.IsValidObject)

        return list(roomSeparationLines)
    
    def GetActiveDesignOptionId(self):
        return DesignOption.GetActiveDesignOptionId(self.doc)

    def GetAllViews(self):
        """
        Get all model views from document
        """
        views =\
            FilteredElementCollector(self.doc)\
            .OfClass(View)\
            .WhereElementIsNotElementType()\
            .Where(lambda x:
                x.IsValidObject
                and not x.IsTemplate)\
        
        return list(views)

    def GetAllViewsTypes(self):
        """
        Collects all views types from model as Dictionary
        """
        viewsTypes =\
            FilteredElementCollector(self.doc)\
            .OfClass(ViewFamilyType)\
            .Where(lambda x: x.IsValidObject)\
        
        return list(viewsTypes)

    def GetAllViewTemplates(self):
        viewTemplates =\
            FilteredElementCollector(self.doc)\
            .OfClass(View)\
            .WhereElementIsNotElementType()\
            .Where(lambda x: 
                x.IsValidObject
                and x.IsTemplate)

        return list(viewTemplates)

    # FIXME: verificar se está funcionando como deve
    def GetAllElementsVisibleInView(self, builtInCat, view):
        """
        Get all elements of BuiltInCategory visible in view
        """
        _elements=\
            FilteredElementCollector(self.doc, view.Id)\
            .OfCategory(builtInCat)\
            .WhereElementIsNotElementType()\
            .Where(lambda x: x.IsValidObject)\

        return list(_elements)

    def GetDocumentPhases(self):
        """
        Get the document phases
        """
        phases =\
            FilteredElementCollector(self.doc)\
            .OfClass(Phase)\
            .WhereElementIsNotElementType()\
            .Where(lambda x: x.IsValidObject)\
        
        return list(phases)

    def GetPhaseIdByName(self, phaseName):
        """
        Gets the Phase Id by its Name
        """
        return\
            self.GetDocumentPhases()\
            .Where(lambda x: x.Name.lower() == phaseName.lower())\
            .FirstOrDefault()\
            .Id

    def GetDocumentPhaseFilters(self):
        phaseFilters =\
            FilteredElementCollector(self.doc)\
            .OfClass(PhaseFilter)\
            .Where(lambda x: x.IsValidObject)\

        return list(phaseFilters)

    def GetFloorTypes(self):
        floorTypes =\
            FilteredElementCollector(self.doc)\
            .OfCategory(BuiltInCategory.OST_Floors)\
            .WhereElementIsElementType()\
            .Where(lambda x: x.IsValidObject)

        return list(floorTypes)

    def ElementLevel(self, item):
        val = None
        if hasattr(item, "LevelId"): 
            val = item.Document.GetElement(item.LevelId)
            if val: return val
        if hasattr(item, "Level"):
            val = item.Level
            if val: return val
        if hasattr(item, "GenLevel"):
            val = item.GenLevel
            if val: return val
        if (item.GetType().ToString() in ("Autodesk.Revit.DB.Architecture.StairsRun", "Autodesk.Revit.DB.Architecture.StairsLanding")):
            item = item.GetStairs()
        if (item.GetType().ToString() == "Autodesk.Revit.DB.Architecture.Stairs"):
            try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.STAIRS_BASE_LEVEL_PARAM).AsElementId())
            except: pass
        if (item.GetType().ToString() == "Autodesk.Revit.DB.ExtrusionRoof"):
            try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.ROOF_CONSTRAINT_LEVEL_PARAM).AsElementId())
            except: pass
        if not val:
            try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.INSTANCE_REFERENCE_LEVEL_PARAM).AsElementId())
            except: 
                try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.INSTANCE_SCHEDULE_ONLY_LEVEL_PARAM).AsElementId())
                except: 
                    try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.SCHEDULE_LEVEL_PARAM).AsElementId())
                    except: return None

    def GetProperlyDynamoRoomCurves(self, DynamoRoom):
        """
        Return all Room curves, including openings
        """
        try:
            roomExternalBoundary = DynamoRoom.CoreCenterBoundary[0]
            
            # Testing Room Curve
            plCurve = DynamoGeometry.PolyCurve.ByJoinedCurves(roomExternalBoundary)
            solid = plCurve.ExtrudeAsSolid(10)
            
            return DynamoRoom.CoreCenterBoundary
        except:
            return DynamoRoom.FinishBoundary

class RevitTaskDialogSettings:
    def __init__(self):
        self.Title = "Checagem de Modelo"
        self.MainIcon = TaskDialogIcon.TaskDialogIconWarning
        self.MainInstruction = None
        self.MainContent = None
        self.ExpandedContent = None
        self.CommonButtons = None
        
class NumberSequenceTools:
    """
    by onBIM Technology
    """

    @staticmethod
    def Range(start=None, end=None, step=None, nearbyStep=None, amount=None):
        """
        Generates a range of values in Arithmetic Progression

         start = the first number of the range
         end = the last number of the range
         step = common difference
         nearbyStep = set true to approximate the step, in order to achieve the end value
         amount = amount of values between start and end

         https://en.wikipedia.org/wiki/Arithmetic_progression
        """
        AP = []

        a1 = start
        an = end
        d = step

        if start is None:
            a1 = 0

        if end is None:
            an = 10

        if start is not None and end is None:
            a1 = 0
            an = start

        if step is None:
            # crescent default step
            d = 1 

            # decrescent default step
            if a1 > an:
            	d = -1 

        # Arithmetic Progression number of elements
        n = (an - a1)/d + 1
        n = round(n)

        if amount is not None and step is None:
            n = float(amount)

            # by forcing n to be float
            # d is prevented to be calculated as integer division
            d = (an - a1) / (n - 1)

        if nearbyStep == True:
            d = (an - a1) / (n - 1)
        
        # Getting digits to round 
        # in order to fix Python float imprecisions
        digits = len(str(float(d)).split('.')[1])
        d = round(d, digits)

        for i in range(1, int(n) + 1):
            ai = a1 + (i - 1)*d
            ai = round(ai, digits)

            # sequence overflow prevention
            if (d > 0 and ai > an) or (d < 0 and ai < an):
                break

            AP.append(ai)

        return AP
    
    @staticmethod
    def Sequence(start, amount, step=None):
        """
        Generates an amount of values in Arithmetic Progression

         start = the first number of the sequence
         amount = amount of numbers to be generated
         step = common difference

         https://en.wikipedia.org/wiki/Arithmetic_progression
        """
        AP = []
        
        a1 = start
        d = step

        if step is None:
            d = 1

        for i in range(1, amount + 1):
            ai = a1 + (i - 1)*d
            AP.append(ai)

        return AP