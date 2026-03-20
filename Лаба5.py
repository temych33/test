class Employee:
 def __init__(self,name,id):
  self.name=name
  self.id=id
 def get_info(self):
  return "Имя: "+self.name+", ID: "+str(self.id)

class Manager(Employee):
 def __init__(self,name,id,department):
  Employee.__init__(self,name,id)
  self.department=department
 def manage_project(self):
  print(self.name+" управляет проектом")

class Technician(Employee):
 def __init__(self,name,id,specialization):
  Employee.__init__(self,name,id)
  self.specialization=specialization
 def perform_maintenance(self):
  print(self.name+" выполняет обслуживание")

class TechManager(Manager,Technician):
 def __init__(self,name,id,department,specialization):
  Manager.__init__(self,name,id,department)
  Technician.__init__(self,name,id,specialization)
  self.team=[]
 def add_employee(self,emp):
  self.team.append(emp)
 def get_team_info(self):
  print("Сотрудники:")
  for emp in self.team:
   print(emp.get_info())

emp1=Employee("Саша",10)
emp2=Employee("Ваня",11)
manager=Manager("Таня",12,"Маркетинг")
tech=Technician("Димон",13,"Оборудование")
tm=TechManager("Азизбек",14,"Аналитика","Данные")
tm.add_employee(emp1)
tm.add_employee(emp2)
tm.add_employee(manager)
tm.add_employee(tech)
tm.manage_project()
tm.perform_maintenance()
tm.get_team_info()
