# SerialiserClass

The Serialiser Class repo provides 3 solution for the question " Write the Json serializer for class object".
This will give then 3 files in the repo whic are solution 1, solution 2 and solution 3.
The description for each solution is given below:

Solution 1:
This solution declares an class Employee. The instance of the employee is created. The jsonifyed output is obatined by applying json.dumps() on the instance of class Employee.

Solution 2:
This solution delares a nested class i.e class Employee is nested inside class Language. Class Employee is initialised in the constructor of class Language. The main method will then create instance of class Language. The json.dumps() method will then provide the json data using lambda function.

Solution 3:
This solution has defined a separate JsonSerializable class. The class language and Employee will then inherit the JsonSerializable class.
The list of instances will then provide the json data of the both classes.
