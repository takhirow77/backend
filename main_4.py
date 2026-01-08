# Что такое exception - Ошибка  -- это ситуация когда python не может продолжать выаолнение 

# int("abc")                 #ValueError
# 10 / 0                     #ZeroDivisionsErro
# user["age"]                #KeyError

# try:
#     age = int(input("Введите Возраст: "))
#     print(age)
# except ValueError:
#     print("Вы ввели не число")


# try:
#     x = int(input())
#     print(10 / x)
# except ValueError:
#     print("Это не число")
# except ZeroDivisionError:
#     print("Делить на ноль нельзя")


# def get_user_age(user):
#     try:
#         return user['age']
#     except KeyError:
#         return None

# user1 = {'name': 'Ivan', 'age': 30}
# user2 = {'name': 'Anna'}

# print(get_user_age(user1))  
# print(get_user_age(user2))  

# def safe_divide(a,b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Деление на ноль"

# def get_age(user):
#     try:
#         return user['age']
#     except KeyError:
#         return "Возраст не указан"


def is_adult(user):
    try:
        return user("age")
    except KeyError:
        return "Возраст не указан"