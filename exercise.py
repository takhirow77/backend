# from main_4 import safe_divide

# try:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     print(safe_divide(a,b))
# except ValueError:
#     print("Вы ввели не число")

# from main_4 import get_age

# user = {"name": "Alex", "age": 25}
# print(get_age(user))

# user2 = {"name": "Maria"}
# print(get_age(user2))

from main_4 import is_adult

try:
    age = int(input("Укажите свой возраст: "))
    print(is_adult(age))
except ValueError:
    print("Вы ввели не число")
