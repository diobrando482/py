# #первая скучнаааа
# def chetniyFilter(numbers):
#     count = {}
#     #кол во входов каждого числа
#     for num in numbers:
#         count[num] = count.get(num, 0) + 1
#     #проверка на четки
#     even_occurrences = [num for num, occurrences in count.items() if occurrences % 2 == 0]
    
#     #ретурнить числа с четным количеством чисел
#     return [num for num in numbers if num in even_occurrences]

# numbers = [1, 2, 3, 2, 2, 3, 3, 1]
# result = chetniyFilter(numbers)
# print(result)
# #вторая 
# def Shitalochka(actions):
#     state = "Nothing"  # дефолтка
    
#     for action in actions:
#         if action == "Like":
#             if state == "Like":
#                 state = "Nothing"  
#             else:
#                 state = "Like"  
#         elif action == "Dislike":
#             if state == "Dislike":
#                 state = "Nothing"  
#             else:
#                 state = "Dislike"  
    
#     return state
# test =["Dislike", "Dislike"]
# print (Shitalochka(test))
#третья
# nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# nums2 = [0, 2, 1, 9, 7]
# nums3 = nums2.copy()

# for num in nums1:
#     if num not in nums2: 
#         nums3.append(num)

# print(nums3)
#девятая
# hours_worked = [8, 8, 8, 0, 8, 8, 8, 8, 0, 0, 8, 8, 8, 8, 8, 0, 8, 8, 8, 0]
# weekly_totals = {}
# daily_averages = []
# current_week_total = 0
# count_of_day = 0
# count_of_week = 1

# for hour in hours_worked:
#     current_week_total += hour
#     count_of_day += 1
#     if count_of_day == 5:
#         weekly_totals[f"Week {count_of_week}"] = current_week_total
#         daily_averages.append(current_week_total / 5)
#         count_of_week += 1
#         current_week_total = 0
#         count_of_day = 0

# total_hours_worked = sum(weekly_totals.values())
# overall_average = total_hours_worked / (len(hours_worked) )

# print("Weekly Totals:", weekly_totals)
# print("Overall Average Hours Worked per Day:", overall_average)
#седьмая задачка
# age = int(input("Введите возраст пользователя: "))

# if age % 2 == 0:
#     numbers = list(range(2, age + 1, 2))
# else:
#     numbers = list(range(1, age + 1, 2))

# print("Вывод:", ", ".join(map(str, numbers)))state = "Nothing"
#пятая задачечка    
# transactions = [
#     "Пополнение через банкомат ~ +1000",
#     "Оплата интернета ~ -500",
#     "Кафе ~ -300",
#     "Зарплата  ~ +15000",
#     "Штраф за парковк ~ -2500",
#     "Подарок ~ +2000"
# ]

# balance = 0

# for transaction in transactions:
#     balance += int(transaction.split(" ~ ")[1])
# print ("Итоговая сумма на счету пользователя:", balance)
# numbers = [1,2,3,4,5,6,7,8,9]
# squares = [n**2 for n in numbers]
# # for n in numbers:
# #     squares.append(n**2)
# print(squares) 
#задача создать новый names_length и переместить туда все имена из списка names но изменить имена сделать заглавными и через тире с именем указать длиину имени




# # names = ['adilet','iskender','sanjar','beknazar']
# # names_length = [f"{n.title()}-{len(n)}" for n in names ]
# # print(names_length)


# #first
# cubes = [x**3 for x in range(1, 101)]
# #second
# odd_numbers = [x for x in range(1, 101) if x % 2 != 0]
# #third
# times_by_5 = [x for x in range(1, 101) if x % 5 == 0]
# #zadacha nomer chetyre
# letters = ["A", "c", "Z", "w", "L", "a", "W", "Q", "i"]
# uppercase_letters = [letter.upper() for letter in letters]

# #five
# str_numbers = ["22", "11", "2", "5", "99", "66", "25", "34", "76"]
# int_numbers = [int(num) for num in str_numbers]
# print(cubes,odd_numbers,times_by_5,uppercase_letters,int_numbers)



# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f"created person with name {self.name}")
#     def __del__(self):
#         print(f"deleted person with name {self.name}")
# tom = Person("tom")
# class Person:
#     def __init__(self, name, age):
#         self.__name = name    # устанавливаем имя
#         self.__age = age       # устанавливаем возраст
                  
#     def print_person(self):
#         print(f"name: {self.__name}\tage: {self.__age}")
          
  
# tom = Person("Tom", 39)
# tom.__name = "Человек-паук"     # пытаемся изменить атрибут __name
# tom.__age = -129                # пытаемся изменить атрибут __
# tom.print_person()
# class Person:
 
#     def __init__(self, name):
#         self.__name = name   # имя человека
 
#     @property
#     def name(self):
#         return self.__name
 
#     def display_info(self):
#         print(f"Name: {self.__name}")
 
 
# class Employee(Person):
 
#     def __init__(self, name, company):
#         super().__init__(name)
#         self.company = company
 
#     def display_info(self):
#         super().display_info()
#         print(f"Company: {self.company}")
 
#     def work(self):
#         print(f"{self.name} works")
 
 
# tom = Employee("Tom", "Microsoft")
# tom.display_info()  # Name: Tom
#                     # Company: Microsoft
# from webbrowser import get


# hello= -5
# # print(hello)
# def get_sum(*args):
#     return sum(args)
# print(get_sum(5,6,7,8,9,0,10))
# print(get_sum(44, 50, 91, 24))

# def get_contact(name, **kwargs):
#     print(f"name: {name}")
#     for key, value in kwargs.items():
#         print(f"{key.title()}: {value}")
        
    
    


# get_contact(
#     "Adilet dokdrubaev",
#     email="luboi@example.com",
#     age=16,
#     birthday="24.10.2007",
#     phone="123-456-789"
# )

# def change_words(*args, **kwargs):
#     prefix = kwargs.get('prefix', '')
#     ending = kwargs.get('ending', '')
#     result = []
#     for word in args:
#         new_word = f'{prefix}_{word}_{ending}'
#         result.append(new_word)    
#     return result


# print(change_words("home", "sun", "school", prefix="lol", ending="master"))


# print(3=='3')
# print({x**2 for x in range(1,6)})
# list = [1,2,3,4,]
# list.append(5)
# print(list)
# set = (1)

# print(set)
# print('hello'+ 5)
# print(5.0//2.0)
# def is_prime(num):
#     if num <= 1:  # Проверка, что число меньше или равно 1 (по определению не является простым)
#         return False
#     for i in range(2, num):  # Перебираем числа от 2 до num - 1
#         if num % i == 0:  # Если число делится нацело, то оно не является простым
#             return False
#     return True  # Если число не делится нацело ни на одно число из диапазона, то оно простое

# # Пример использования:
# print(is_prime(19))

import requests
def quote_generate():
    response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
    data = response.json()
    author = data["quoteAuthor"]
    quote = data["quoteText"]
    return  author, quote

author, quote = quote_generate()
print("author",author)
print('quote',{quote})