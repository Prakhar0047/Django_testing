import random

salary = [50000, 60000, 55000, 70000, 65000, 80000]

def add_salary():
    sl = random.choice(salary)
    return sl

x = add_salary()

print(x)