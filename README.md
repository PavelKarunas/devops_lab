# Python module

# Pavel_Karunas_Day5 Traversing Directories and Unit Tests

**Description: Traversing Directories Task1 App**
1. This application can take following parameters at start:
	- --parent (required)(self exclusive with recursive parameter)
	- --recursive (required)(self exclusive with parent parameter)
	- --extension (optional)
	- --path (optional)
	- --byname (optional)(self exclusive with bydate parameter)
	- --bydate (optional)(self exclusive with byname parameter)

2. Parent parameter determines search scope, search for files will be held only in parent folder if specified (cant be used with recursive parameter)(mandatory parameter).
3. Recursive parameter determines search scope, search for files will be held recursively over all child folders if specified (cant be used with parent parameter)(mandatory parameter).
4. Extension parameter can be used to narrow down file search to specific file format e.g. txt, json, py.
5. Path parameter if used, indicates desired path in which application will search for files (by default search will be held in current directory (./) ).
6. Byname parameter if used, sorts files in alpabetical order (cant be used with bydate parameter).
7. Bydate parameter if used, sorts files by time of last modification (cant be used with byname parameter).
8. Application after being invoked list files accordingly to parameter your choose.


**Requirements:**

Python version 3.6 or above


**Examples of use:**

$ task1.py --help

$ task1.py --parent --extension txt --byname

$ task1.py --parent --bydate

$ task1.py --parent --extension py --path /home/student/Python/Hometask/ --byname

$ task1.py --recursive

$ task1.py --recursive --extension html

$ task1.py --recursive --bydate --extension json --path /home/student



**Description: Unit Tests Task2 App**
1. Reads an integer. For all non-negative integers i lesser than N, prints N squared by 2.
2. Unit tests for this script stored in test_task2.py (two files should be in same folder).
3. Two checks are applyed **self.assertEqual(task2.square_list(5), [0, 1, 4, 9, 16])** and **self.assertRaises(ValueError, task2.square_list, -4)**.
4. First check examine function for valid results, second confirms appropriate exception if negative number are thrown into function.
5. Nosetests --with-coverage shows 73% code coverage.

**Requirements:**

Python version 3.6 or above

pip install nose

pip install coverage


**Examples of use:**

$ python test_task2.py

$ python -m unittest test_task2.py

$ nosetests test_task2.py

$ nosetests --with-coverage --cover-html test_task2.py


