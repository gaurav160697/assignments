class Student:
    def __init__(self):
        self._name = ""
        self._rollNumber = ""
        
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
        
    def getRollNumber(self):
        return self._rollNumber
    
    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber
student = Student()
student.setName("John")
student.setRollNumber("12345")
print(student.getName())
print(student.getRollNumber())
