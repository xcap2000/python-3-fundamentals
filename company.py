# from file import class
from employee import SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('--------------------')

    def pay_employees(self):
        print('Paying Employees:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('--------------------')

def main():
    company = Company()

    employee1 = SalaryEmployee('Sarah', 'Hess', 50000)
    company.add_employee(employee1)
    employee2 = HourlyEmployee('Lee', 'Smith', 25, 50)
    company.add_employee(employee2)
    employee3 = CommissionEmployee('Bob', 'Brown', 30000, 5, 200)
    company.add_employee(employee3)
    
    # print(company.employees)

    company.display_employees()
    company.pay_employees()

main()