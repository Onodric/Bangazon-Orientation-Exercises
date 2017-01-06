# Classes

## Instructions

# Create a class that contains information about employees of a company and define methods to get employee name, job title, and start date.

class Company(object):
    '''
    Contains methods for emplyee tracking in a company

    Methods
    =======
    getName
    getJobTitle
    getStartDate
    '''

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def getName(self):
        '''
        Returns the employee's name
        '''
        return self.name

    def getJobTitle(self)
        '''
        Returns the employee's job title
        '''
        return self.title

    def getStartDate(self)
        '''
        Returns the employee's start date
        '''
        return self.start_date

    # Add the remaining methods to fill the requirements above
