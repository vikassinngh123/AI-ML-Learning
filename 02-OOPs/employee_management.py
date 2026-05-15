
def is_input_valid(mini=None,maxi=None,msg="input"):
  while True:
    try:
      value=int(input(f"{msg}"))
      if mini is not None and maxi is not None:
        if mini<=value<=maxi:
          return value
        else:
          print(f"Invalid Input enter a value between {mini} and {maxi}")

      return value
    except ValueError:
        print("invalid Input! please enter a number not text.")


class employee:
  def __init__(self,employee_id,name,age,salary,department):
    self.employee_id=employee_id
    self.name=name
    self.age=age
    self.salary=salary
    self.department=department

  def __str__(self):
    return f"employee_id={self.employee_id} name={self.name} age={self.age} salary={self.salary} department={self.department}"

  def __repr__(self):
    return f"employee_id={self.employee_id} name={self.name} age={self.age} salary={self.salary} department={self.department}"


class manager(employee):
  def __init__(self):
    self.employees=[]
  
  def add_employee(self):
    print("-----Enter the details of Employee-----")
    while True:
      employee_id=is_input_valid(1,9999999,"Enter the employee id : ")
      if employee_id in [emp.employee_id for emp in self.employees]:
        print("Employee id already exists")
      else:
        break 
    
    name=input("Enter the name of Employee : ")
    age=is_input_valid(18,100,"Enter the age of Employee : ")
    salary=is_input_valid(0,999999999,"Enter the salary of Employee : ")
    department=input("Enter the department of Employee : ")

    self.employees.append(employee(employee_id,name,age,salary,department))
    print(f"Employee {name} added successfully")

  def list_of_employees(self):
    if len(self.employees)==0:
      print("There is no data on employee")
      return
    else:
      for emp in self.employees:
        print(emp)

  # Funtion if we want to find multiple employees of same name
  def searching_employee(self,name):
    if len(self.employees)==0:
      print("There is no data on employee")
    else:
      number=1
      for emp in self.employees:
        if emp.name.lower()==name.lower():
          number+=1
          print(emp)
        
      if number==1:
        print("Employee not found")
      else:
        print(f"{number-1} Employee found")

   # Funtion if we want to find specific employee(by emp_id) for updating or deleting
  def update_employee(self,emp_id):
     if len(self.employees)==0:
      print("There is no data on employee")
     else:
       for emp in self.employees:
         if emp.employee_id==emp_id:
           print(emp)
          
           print("Enter the updated details of Employee")

           emp.name=input("Enter the name of Employee : ")
           emp.age=is_input_valid(18,100,"Enter the age of Employee : ")
           emp.salary=is_input_valid(0,999999999,"Enter the salary of Employee : ")
           emp.department=input("Enter the department of Employee : ")

           print("Employee updated")

       else:
          print("Employee not found")

  def delete_employee(self,emp_id):
        if len(self.employees)==0:
          print("There is no data on employee")
        else:
          for emp in self.employees:
            if emp.employee_id==emp_id:
              self.employees.remove(emp)
              print("Employee deleted")
              break
          else:
            print("Employee not found")


def main():
    
    my_manager = manager() 

    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            my_manager.add_employee()
        elif choice == '2':
            my_manager.list_of_employees()
        elif choice == '3':
            name = input("Enter name to search: ")
            my_manager.searching_employee(name)
        elif choice == '4':
            emp_id = is_input_valid(0,9999999,"Enter ID to update: ")
            my_manager.update_employee(emp_id)
        elif choice == '5':
            emp_id = is_input_valid(0,9999999,"Enter ID to delete: ")
            my_manager.delete_employee(emp_id)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
