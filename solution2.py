import json

class Language():
    def __init__(self, lname,name,designation):
        self.lname = lname
        self.employee = self.Employee(name=name,designation=designation)

    class Employee:
        def __init__(self, name, designation):
            self.name = name
            self.designation = designation


if __name__ == '__main__':
    L1 = Language('python','akshay','developer')
    print(json.dumps(L1,default= lambda o:o.__dict__,indent=4))




"""
This is the output of main program
{
    "lname": "python",
    "employee": {
        "name": "akshay",
        "designation": "developer"
    }
}
"""

