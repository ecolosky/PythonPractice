from Person import Person
from datetime import date

Edward = Person('Edward', 'Colosky', date(1994,4,4))
Caroline = Person('Caroline', 'Brunson', date(1994,8,8))

print(f'{Edward}')
print(f'{Caroline}')
print("Are Ed and Caroine the same age?: ")
print(Edward == Caroline)