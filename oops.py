#class,objects,methods,constructor,destructor
class Employee:
    attr="company"      #class attribute
    def __init__(self,name):      #instance attribute-name
        self.name=name
    def speak(self):
        print(f"{self.name} is in company")
    def __del__(self):
        print("destructor called.")
    
    
emp=Employee("tanya")
emp.speak()
print(emp.name)
print(emp.__class__.attr)
print(emp.attr)
