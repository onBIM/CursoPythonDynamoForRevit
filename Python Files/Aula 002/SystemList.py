# by onBIM Technology
# www.onbim.net
# file name: ./Python Files/Aula 002/SystemList.py

import clr
import traceback

# Import System Libraries
import System
clr.AddReference("System.Core")
from System.Collections.Generic import List as SystemList
from System.Collections.Generic import HashSet
from System.Collections.Generic import Dictionary

myPython_Numbers = [1, 2, 3, 4, 5, 5, 3, 1]

numeros = HashSet[int](myPython_Numbers)

myDotNet_Dictionary = Dictionary[str, int]()
myDotNet_Dictionary["one"] = 1
myDotNet_Dictionary["two"] = 2
myDotNet_Dictionary["three"] = 3

print(myDotNet_Dictionary)
