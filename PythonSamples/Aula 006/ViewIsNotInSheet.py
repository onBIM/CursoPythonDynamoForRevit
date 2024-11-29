# by onBIM Technology
# www.onbim.net
# file name: ./Aula 006/ViewIsNotInSheet.py

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
    
    viewports = \
        FilteredElementCollector(doc) \
        .OfClass(Viewport) \
        .WhereElementIsNotElementType() \
        .ToElements()
    
    # Com List Comprehension
    # viewIdsInSheets = [
    #     vp.ViewId
    #     for vp in viewports
    # ]
    
    viewIdsInSheets = viewports.Select(lambda vp: vp.ViewId)
    
    viewsNotInSheets = \
        FilteredElementCollector(doc) \
        .OfCategory(BuiltInCategory.OST_Views) \
        .WhereElementIsNotElementType() \
        .Where(
            lambda view:
            view is not None
            and not view.IsTemplate
            and view is not ViewSheet
            and view.Id not in viewIdsInSheets
            and len(view.GetDependentViewIds()) == 0
        ) \
        .Select(lambda view: view.ToDSType(True))
    
    result = viewsNotInSheets
    
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