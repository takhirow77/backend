# def say_hello():
#     print('Hello!')

# say_hello()                          #вызов функций


# def greet(name):
#     print(f'Привет, {name}')

# greet('Alex')
# greet('Maria')

# def sum_numbers(a,b):
#     return a + b                                  #return - возвращает результат и останавливает функцию

# result = sum_numbers(5,3)
# print(result)


# def chek_age(age):
#     if age >= 18:
#         return "Доступ разрешен"
#     else:
#         return "Доступ запрещен"
    
# print(chek_age(20))

# def authenticate(user,password):
#     if user == "admin" and password == "1234":
#         return True
#     return False

# def is_adult(age):
#     if age >= 18:
#         return True
#     return False

# print(is_adult(18))

# def get_even_numbers(numbers):
#     even_numbers = []

#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)
    
#     return even_numbers

# print(get_even_numbers([10,3,2,16,4,7,8]))

# def get_user_names(users):
#     user_names = []

#     for user in users:
#         if user['age'] >= 18:
#             user_names.append(user["name"])

#     return user_names

# print(get_user_names([{"name": "Alex", "age": 17}]))
# print(get_user_names([{"name": "Maria", "age": 22}]))