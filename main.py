# print("Hello, Backend")

# name = 'Hojiakbar'   #строка (str)
# age = 18             #число (int)
# height = 1.80        #число с точкой (Float)
# is_student = True    #Логический тип (bool)

# print(name,age,height,is_student)


# name  = input('Как тебя зовут? -  ')  #input  всегда возращает строку 
# print("Hello", name)

# name1 = input('Как тебя зовут? -  ')
# age = int(input("Сколько тебе лет? - "))

# print('Hello', {name1}, {age})


# age = (int(input("Введите возраст - ")))

# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")


# age = (int(input(f"Введите возраст - ")))

# if age < 18:
#     print("Ребенок")
# elif age < 60:
#     print("Взрослый")
# else:
#     print("Пенсионер")

# age = (int(input('Введите возраст: ')))
# has_passport = True

# if age >= 18 and has_passport:
#     print("Можно войти")
# else:
#     print("Вход запрещен")


# username = (input("Введите ваш username: "))
# password = (int(input("Введите пароль: ")))

# if username ==  username and password == password:
#     print("Успешный вход")
# else:
#     print("Неверные данные")


# age = (int(input("Введите возраст: ")))

# if age < 18:
#     print("Вход запрещен")
# elif 18 <= age <= 60:
#     print("Добро пожаловать")
# else:
#     print("Добро пожаловать, уважаемый пользователь")

# age = (int(input("Введите возраст: ")))
# has_passport = input("Есть паспорт? - ").strip().lower() in ("да", "yes", "y")

# if age >= 18 and has_passport:
#     print("Вход разрешен")
# else:
#     print("Вход запрещен")

# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print(i)

# users = ['admin', 'user1', 'user2']

# for user in users:
#     print(user)

# for i in range(1,11):
#     print(i)

# count = 0 

# while count < 5:
#     print(count)
#     count += 1

# password = ""

# while password != "1234":
#     password = input("Введите пароль: ")

# print("Доступ разрешен")

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# users = ["admin", "manager", "guest"]

# for user in users:
#     if user == "admin":
#         print("Администратор  найден")
#         break


# attempts = 3 

# while attempts > 0:
#     password  = input("Введите пароль: ")
#     if password == "admin123":
#         print("Вход выполнен")
#         break
#     else:
#         attempts -= 1
#         print("Неправильный пароль")

# if attempts == 0:
#     print("Слишко много попыток")



# numbers  = [1,4,7,10,15]

# for number in numbers:
#     if number % 2 == 0:
#         print(number)


# users = ['admin', 'user1', 'user2']               #список

# users.append('guest')              # добавить
# users.append('guest1')             # удалить
# users.remove('user1')              # длина
# print(len(users))

# print(users[0])                      #выводить по индексу


# for user in users:
#     print(user)


# user = {                                        #словарь(dict)
#     "id": 1,
#     "name": "Alex ",
#     "age": 25,
#     "is_active": True   
# }

# print(user["name"])

# user["age"] = 26
# user["email"] = "alex@gmail.com"

# print(user['email'])

# for key, value in user.items():         #чтобы ввести через цикл что в внутри словаря(dict)
#     print(key, value)

# responce = {

#     'status': 'ok',
#     'date':{
#         'id': 1,
#         'name': 'Alex'
#     }
# }

# users = ['admin', 'user1', 'user2']

# users.append('guest')
# print(users)


# user = {
#     "name": "Alex",
#     "age": 25,
#     "email": "alex@mail.com"
# }

# print(user["name"])
# print(user["email"])

# users = [

#     {'name': 'Alex', 'age': 17},
#     {'name': 'Maria', 'age': 22},
#     {'name': 'Ivan',   'age': 30}
# ]

# for user in users:                              # берём одного пользователя
#     if user['age'] > 18:                        # смотрим его возраст
#         print(user['name'])                     # выводим имя