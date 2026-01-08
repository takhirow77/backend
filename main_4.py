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


def get_user_age(user):
    try:
        return user['age']
    except KeyError:
        return None

user1 = {'name': 'Ivan', 'age': 30}
user2 = {'name': 'Anna'}

print(get_user_age(user1))  # 30
print(get_user_age(user2))  # None
