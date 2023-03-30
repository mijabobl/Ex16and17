#using person as parent class
class Person:
  def __init__(self, fname, lname, dob):
    self.firstname = fname
    self.lastname = lname
    self.dob = dob

#employee is inheriting Person
class Employee(Person):
  def __init__(self, fname, lname, dob, empnum):
    super().__init__(fname, lname, dob)
    self.employeenum = empnum
  def printer(self):
    print("Employee Name: ", self.firstname, self.lastname, "  Dob.....", self.dob, "  Employee Number.....", self.employeenum)

#Customer also inherits person
class Customer(Person):
  def __init__(self, fname, lname, dob, custnum):
    super().__init__(fname, lname, dob)
    self.customernum = custnum

  def printer(self):
    print("Customer Name", self.firstname, self.lastname, "  Age.....", self.dob, "  Customer Number.....", self.customernum)