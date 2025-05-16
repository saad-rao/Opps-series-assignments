class Employee:
    def __init__(self,name,salary,snn):
        self.name= name   #public
        self.__snn= snn   #private
        self._salary= salary #protected
        
emp = Employee("Ali",50000,123456789)

print(emp.name) # public it prints the name
print(emp.__snn) # private  Shows error coz it is private  
print(emp._salary) # protected It prints the salary
