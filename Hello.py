print("hello python")

def ind(id = 101):
    print(id)
ind()

class Emp:
    offi_add = 'bengalore'
    def __init__(self, name, age, sal):
        self.name = name
        self.age = age
        self.sal = sal
    def get_emp_details(self):
        print("Emp details are:",self.name,self.age,self.sal,self.offi_add)
obj = Emp('sarath',23,234445)
obj.get_emp_details()


