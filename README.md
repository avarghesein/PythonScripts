# PythonScripts
Python Scripting Samples (written and tested in Visual Studio)

# Setup Development Environment
* Install Visual Studio 2013+
* Install Python 3.7+
* Install Python Tools For Visual Studio (Through Extensions in Visual Studio)
* Setup Python 3.7 Environment through Visual Studio Tools/Options/Python Tools Menu
![alt EnvSettingPythonInVS](https://github.com/avarghesein/PythonScripts/blob/master/Scripts/PythonEnvVSSetting.jpg)
* Unit Test through Visual Studio Test Explorer
![alt UnitTestPythonInVS](https://github.com/avarghesein/PythonScripts/blob/master/Scripts/PythonVSUnitTest.jpg)

# Scripts
# 1. [FindWorkShiftByDate/FindWorkShiftByDate.py](https://github.com/avarghesein/PythonScripts/blob/master/Scripts/FindWorkShiftByDate/FindWorkShiftByDate.py)
Finds working shifts, given a date range. Shift slots below, which can be configured in the source file.

    12:00 AM - 08:30 AM (Prev-Day Night Shift-3)
    08:31 AM - 06:30 PM (Day Shift-1)
    06:31 PM - 10:30 PM (Second Shift-2)
    10:31 PM - 11:59 PM (Night Shift-3)
    
See test cases written in [FindWorkShiftByDate/FindWorkShiftByDate_test.py](https://github.com/avarghesein/PythonScripts/blob/master/Scripts/FindWorkShiftByDate/FindWorkShiftByDate_test.py)

# 2. [MatrixOperations/MatrixOperations.py](https://github.com/avarghesein/PythonScripts/blob/master/Scripts/MatrixOperations/MatrixOperations.py)
Simple matrix operations using 2D List and List Comprehensions.

    #Matrix Format (With Column and Row headers support)
    [["Person/Stock","Product1", "Product2","Product3"],
     ["John",100, 20, 30],
     ["Keith",20, 40, 10],
     ["Russel",20, 60, 20]]
     
    #Columnwise Sum
    [["John",150], ["Keith",70],["Russel",100]]
    
    #Rowwise Sum
    [["Product1",140], ["Product2",120],["Product3",60]]
    
See test cases written in [MatrixOperations/MatrixOperations_Test.py](https://github.com/avarghesein/PythonScripts/blob/master/Scripts/MatrixOperations/MatrixOperations_Test.py)
