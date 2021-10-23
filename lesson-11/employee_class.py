class Employee(object):
  """Models real-life employees!"""

  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00


class PartTimeEmployee(Employee):
  def __init__(self, employee_name):
    super(PartTimeEmployee, self).__init__(employee_name)

  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00


milton = PartTimeEmployee('milton')
print(milton.full_time_wage(10))
