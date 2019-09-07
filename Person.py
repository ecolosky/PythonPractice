from datetime import date, timedelta

class Person:
    daysInAYear = 365
    def __init__(self, firstName, lastName, dob):
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dob
    def __format__(self, format_spec):
        return "{0}, {1} \n {2:.0f} years old \n".format(self.lastName, self.firstName, self.getAge())

    def __eq__(self, other):
        return int(self.getAge()) == int(other.getAge())

    def getAge(self):
        return (date.today() - self.dateOfBirth).days/self.daysInAYear
