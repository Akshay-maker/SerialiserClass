import json


class Employee:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation


E1 = Employee('Akshay','Developer')

if __name__ == '__main__':
    response = json.dumps(E1.__dict__,indent=4) #Serialize obj to a JSON formatted str
    print(response)




"""
This is the output of main program
response = {
                "name": "Akshay",
                "choice": "Python"
           }
"""
