# class User:
#     pass  # этот класс ничего не делает
#
# peter = User()
# peter.name = "Peter Robertson"
#
# julia = User()
# julia.name = "Julia Donaldson"
#
# print(peter.name)
# print(julia.name)
#
# peter.email = "peterrobertson@mail.com"
# print(peter.email)
# print('\n')
# # print(julia.email)
#
# class User:
#     number_of_fingers = 5
#     number_of_eyes = 2
#
# lancelot = User()
# print(lancelot.number_of_fingers)


# 21.4. Магический метод __init__

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
# peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
# julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")
#
# print(peter.name)
# print(julia.email)

# Peter Robertson
# juliadonaldson@mail.com

#  21.6. Наследование

# import datetime
#
# class Product:
#     max_quantity = 100000
#
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False
#
# class Food(Product):
#     is_critical = True
#     needs_to_be_refreshed = True
#     refresh_frequency = datetime.timedelta(days=1)
#
# eggs = Food(name="eggs", category="food", quantity_in_stock=5)
# print(eggs.max_quantity)
# print(eggs.is_available())


# class Event:
#     def __init__(self, timestamp=0, event_type="", session_id=""):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
#
#     def show_description(self):
#         print("This is generic event.")
#
#
# class ItemViewEvent(Event):
#     type = "itemViewEvent"
#
#     def __init__(self, timestamp=0, session_id="", number_of_views=0):
#         self.timestamp = timestamp
#         self.session_id = session_id
#         self.number_of_views = number_of_views
#
#     def show_description(self):
#         print("This event means someone has browsed an item.")
#
#
# if __name__ == "__main__":
#     test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", number_of_views=6)
#     test_view_event.show_description()
#     print(test_view_event.type)


#  21.7. Наследование класса

# A Python program to demonstrate inheritance

# class Person(object):
#     # Constructor
#     def __init__(self, name, id):
# 	    self.name = name
# 	    self.id = id
#
# # To check if this person is an employee
#     def Display(self):
# 	    print(self.name, self.id)
#
# # Driver code
# emp = Person("Satyam", 102) # An Object of Person
# emp.Display()
#
# class Emp(Person):
#     def Print(self):
#         print("Emp class called")
#
# Emp_details = Emp("Mayank", 103)
#
# # calling parent class function
# Emp_details.Display()
#
# # Calling child class function
# Emp_details.Print()


# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


# class Person(object):
# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name
#
# 	# To get name
# 	def getName(self):
# 		return self.name
#
# 	# To check if this person is an employee
# 	def isEmployee(self):
# 		return False
#
# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):
# 	# Here we return true
# 	def isEmployee(self):
# 		return True
#
# # Driver code
# emp = Person("Geek1") # An Object of Person
# print(emp.getName(), emp.isEmployee())
#
# emp = Employee("Geek2") # An Object of Employee
# print(emp.getName(), emp.isEmployee())


