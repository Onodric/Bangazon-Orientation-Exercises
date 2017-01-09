#--------|---------|---------|---------|---------|---------|---------|---------
# Classes

## Instructions

# Create a class that contains information about employees of a company and define methods to get employee name, job title, and start date.

class Company(object):
    '''
    Contains methods for employee tracking in a company

    Methods
    =======
    get_name
    get_job_title
    get_start_date
    '''

    def __init__(self, company_name, employees=[]):
        self.name = company_name
        self.employees = employees

    def add_employee(self, employee):
        self.employees.add(employee)

    def get_employees(self):
        return self.employees

    def __str__(self):
        employee_list = '{} Employee List\n-------------------------'.format(self.name)
        for employee in self.employees:
            employee_list += '\n{}'.format(employee)
        return employee_list

    # Add the remaining methods to fill the requirements above


class Employee(object):

    def __init__(self, first_name, last_name, job_title="Minion", start_date="1 Jan 1990", ):
        self.first_name = first_name
        self.last_name = last_name
        self.title = job_title
        self.start_date = start_date

    def get_name(self):
        '''
        Returns the employee's name
        '''
        full_name = self.first_name + " " + self.last_name
        return full_name

    def set_job_title(self, job_title):
        self.title = job_title

    def get_job_title(self):
        '''
        Returns the employee's job title
        '''
        return self.title

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_start_date(self):
        '''
        Returns the employee's start date
        '''
        return self.start_date

    def __str__(self):
        employee_str = '{0}, {1}, started {2}'.format(self.get_name(), self.get_job_title(), self.get_start_date())
        return employee_str

matt = Employee("Matt", "McCord", "Badass", "2 Jan 2017")
ben = Employee("Ben", "Marks", "Minion",  "2 Jan 2017")
nate = Employee("Nathan", "Baker", "Hoopty", "2 Jan 2017")
steve = Employee("Steve", "Brownlee", "Owner")
bang_employees = [matt, ben, nate, steve]

c16_fake_co = Company("Bangazon, LLC", bang_employees)

print(c16_fake_co)

# 3. Consider the concept of [aggregation](../FND_09_INHERIT_COMPOSE_AGGREGATE.md#aggregation), and modify the `Company` class so that you assign employees to a company. 
# 4. Create a company, and three employees, and then assign the employees to the company.