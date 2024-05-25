# import random
# #виселица
# def choose_word():
#     words = ["apple", "banana", "cherry", "orange", "grape"]
#     return random.choice(words)

# def display_word(word, guessed_letters):
#     display = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display += letter
#         else:
#             display += "_"
#     return display

# def hangman():
#     word = choose_word()
#     guessed_letters = []
#     attempts = 6

#     print("Welcome to Hangman!")
#     while True:
#         print(display_word(word, guessed_letters))
#         guess = input("Guess a letter: ").lower()

#         if guess in guessed_letters:
#             print("You already guessed that letter.")
#         elif guess in word:
#             guessed_letters.append(guess)
#             if display_word(word, guessed_letters) == word:
#                 print("Congratulations! You guessed the word: " + word)
#                 break
#         else:
#             attempts -= 1
#             print("Incorrect guess. Attempts left:", attempts)
#             if attempts == 0:
#                 print("You ran out of attempts. The word was:", word)
#                 break

# hangman()
# # print("Привет, мир!")
# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))

# sum = num1 + num2
# print("Сумма чисел равна:", sum)
# num = int(input("Введите число: "))

# if num % 2 == 0:
#     print("Число", num, "является четным.")
# else:
#     print("Число", num, "является нечетным.")
# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
# num3 = float(input("Введите третье число: "))

# max_num = max(num1, num2, num3)
# print("Наибольшее число:", max_num)
# for i in range(1, 11):
#     for j in range(1, 11):
#         result = i * j
#         print(f"{i} x {j} = {result}")
# year = int(input("Введите год: "))

# if (year % 4 == 0 and year % 100 != 0):
#     print(year, "год является високосным.")
# else:
#     print(year, "год не является високосным.")
# numbers = []
# for i in range(5):
#     num = float(input(f"Введите {i+1}-е число: "))
#     numbers.append(num)

# average = sum(numbers) / len(numbers)
# print("Среднее значение чисел:", average)
# num = int(input("Введите число: "))
# num = 345
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "не является простым числом.")
#             break
#     else:
#         print(num, "является простым числом.")
# else:
#     print(num, "не является простым числом.")
# gradus = float(input("Введите температуру в градусах Цельсия: "))
# far = (gradus * 9/5) + 32
# print("temperature in far:", far)
# import math

# radius = float(input("Введите радиус круга: "))
# area = math.pi * radius**2
# print("Площадь круга с радиусом", radius, "равна", area)
# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib = fibonacci(n - 1)
#         fib.append(fib[-1] + fib[-2])
#         return fib

# n = int(input("Введите количество чисел Фибоначчи: "))
# fibonacci_sequence = fibonacci(n)

# print("Последовательность чисел Фибоначчи:")
# print(fibonacci_sequence)
# def find_intersection(arr1, arr2):
#     intersection = []
#     for element in arr1:
#         if element in arr2 and element not in intersection:
#             intersection.append(element)
#     return intersection

# array1 = [1, 2, 3, 4, 5]
# array2 = [3, 4, 5, 6, 7]
# result = find_intersection(array1, array2)
# print(result)
# allowed_usernames = ["hello1", "oleg66", "ali55", "killer07"]

# def check_permission(func):
#     def wrapper(username):
#         if username in allowed_usernames:
#             func(username)
#         else:
#             print("u tebya netu prav.")
#     return wrapper

# @check_permission
# def greet_user(username):
#     print("Hello", username)


# greet_user("oleg66")  
# greet_user("john")    
# greet_user('hello 1')
# greet_user('Dilyar temnii bro')
# greet_user('feministka')
# def find_max(arr):
#     return max(arr)

# print(find_max([1, 5, 3, 9, 2]))  # 9
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# print(is_prime(7))   # True
# print(is_prime(12))  # False
# def find_average(arr):
#     return sum(arr) / len(arr)

# print(find_average([1, 2, 3, 4, 5]))  # 3.0
# def count_words(s):
#     return len(s.split())

# print(count_words("Hello, World!"))  # 2
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))  # 4
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("racecar"))  # True
# # print(is_palindrome("hello"))    # False
# def reverse_number(num):
#     return int(str(abs(num))[::-1]) 

# print(reverse_number(123))   # 321
# def find_lcm(a, b):
#     def gcd(x, y):
#         return x if y == 0 else gcd(y, x % y)
    
#     return (a * b) // gcd(a, b)

# print(find_lcm(12, 15))  
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# print(factorial(5))  # 120

# import requests
# def quote_generate():
#     response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
#     data = response.json()
#     author = data["quoteAuthor"]
#     quote = data["quoteText"]
#     return  author, quote

# author, quote = quote_generate()
# print("author",author)
# print('quote',{quote})
# #app makes random quotes created by me

#классы методы обьекты методы атрибуты



# class Car:
#     def __init__(self,model,color ,price,year, speed, tank=60):
#         self.model = model
#         self.color = color
#         self.price = price
#         self.year = year
#         self.speed = speed
#         self.tank = tank
    
#     def get_info(self):
#         return f"{self.model} {self.color} {self.price} {self.year} {self.speed} {self.tank}"
    
#     def sell_car(self,new_owner):
#         self.owner = new_owner
#         print(f"{self.model} sold to {self.owner}")
#     def start(self):
#         self.engine = True
#         print("двигатель включен")
#     def stop(self):
#         self.engine = False
#         print('двигатель включен')
        