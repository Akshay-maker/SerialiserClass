import json


class JsonSerializable:
    def toJson(self):
        return json.dumps(self,default=lambda o:o.__dict__, indent=4)

    def __repr__(self):
        return self.toJson()


class Language(JsonSerializable):
    def __init__(self, lname):
        self.lname = lname


class Employee(JsonSerializable):
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation


L1 = Language('python')
E1 = Employee('Akshay','Developer')

if __name__ == '__main__':
    response = [L1,E1]
    print(response)

"""
Output:
[{
    "lname": "python"
}, {
    "name": "Akshay",
    "choice": "Python"
}]
"""