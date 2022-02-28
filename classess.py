# class resturant:
#         def _init_ (self, salads, burgers,steaks):
#             self. salads = salads
#             self. burgers = burgers
#             self. steaks = steaks
#             self. is_started = False
#             self. toppings = []
            
#         def add_topping(self,topping):   
#             self.toppings.push(topping) 

# tyrones_car = Car("lexus","ls")
# troys_car = Car ('Ford','Explorer')

# troys_car.start_engine()

# print(tyrones_car)

# class Employee:
#     def __init__(self,first, last , paycheck):
#         self.first = first
#         self.last = last
#         self.paycheck = paycheck
#         self.email = first + '.' + last + ' @company.com '

#         def fullname(self):
#             return '{} {}'.format(self.first, self.last)

# emp_1 = Employee('Jemale', 'Jones', 50000)
# emp_2 = Employee('William', 'Smith', 60000)


# print(emp_1.email)
# print(emp_2.email)

from curses import ACS_GEQUAL


class puppys:
    def __init__(self,name,sex, age):
        self.name = name
        self.sex = sex
        self.age = age
    
    def fullname(self):
        return '{} {}'. format (self.name, self.sex)

puppys_1 = puppys('Bella','female', 7)
puppys_2 = puppys('Max', 'male', 3)

print(puppys_1.name, puppys_1.age)
print(puppys_2.age)

