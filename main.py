# num1 = int(input())
# num2 = int(input())
# oper = input()

# if oper == "+":
#     print(num1 + num2)
# # elif oper == "-":
#     print(num1 - num2)
# elif oper == "/":
#     print(num1 / num2)
# elif oper == "*":
#     print(num1 * num2)
# else:
#     print("error")

# for i in range(1,20):
#     print(i)

# print(list[0])
# for i in range(2,100, 2):
#     print(i)



# for i in range(1,20):
#     print(i)
    
# sum = 0  

# for number in range(1, 101):
#     sum += number

# print(sum)


# n = int(input("Введите целое число n: "))


# if n < 0:
#     print("число отрицательное")
# elif n == 0:
#     print("Факториал числа 0 равен 1.")
# else:
#     factorial = 1 
#     for i in range(1, n + 1):
#         factorial *= i 
#     print(f"Факториал числа {n} равен {factorial}")
# num = int(input("Введите целое число: "))


# if num <= 1:
#     is_prime = False
# else:
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break


# if is_prime:
#     print(f"{num} - простое число")

# for i in range(1, 10):
#         result = i * 5 
#         print(f"{i} * 5 *  = {result}")
# time = input("Enter the time (hh:mm): ")
# hours = int(time[:2])
# time_of_day = ""

# if 5 <= hours < 12:
#     time_of_day = "Morning"
# elif 12 <= hours < 18:
#     time_of_day = "Afternoon"
# elif 18 <= hours < 22:
#     time_of_day = "Evening"
# else:
#     time_of_day = "Night"

# print(f"The time of day is: {time_of_day}")
# for x in range(1, 11):
# 	for y in range(1, 11):
# 		print(x * y =  x * y, end="\n")
# 	print()
# for x in range(1, 11):
# 	for y in range(1, 11):
# 		print(x, "*", y, "=", x * y, end="\n")
# 	print()
# num1 = int(input("WWEDITE"))
# num2 = int(input("WWEDITE"))
# while True:
#     znak = input("wwedite znak")
#     if znak == "+":
#         print("Resultat:",num1 + num2)
#         break
#     elif znak == "-":
#         print("Resultat:",num1 - num2)
#         break
#     elif znak == "*":
#         print("Resultat:",num1 * num2)
#         break
#     elif znak == "/":
#         print("Resultat:",num1 / num2)
#         break
#     else:
#         print("Ti eblan, wwedi norm znak")
#обьедените две строки в одну
# a = "Hello"
# b = "Adilet"
# print(a + b)

# original_string = "patata"
# changed_string = ''

# for i in original_string:
#     if i == 'a':
#         changed_string += 'e'
#     else:
#         changed_string += i

# print(changed_string)
# # b = "Adilet"
# # print(
# for i in range(1, 11):

#     print(i)


# num = int(input())


# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")

# for i in range(2,12,2):
#    print(i)
# num1 = int(input())
# if num1<18:
#     print("малолетка")
# if num1>18:
#     print("совершенолет")

# for i in range(1, 11):
#     for y in range(1,11):
#         print(f"{i}*{y} = {i*y}")

# for i in range(1,1000001):
#     print(i)
    
    # list = [1,2,3,4,5,6,7]

    # def sum_of_items(nums):
    #     a = 0
    #     nums +=a
    #     print (a)
# my_list = [1, 2, 3, 4, 5]
# def find_sum(lst):
#     total_sum = sum(lst)
#     return total_sum

# def multiply_list(lst, factor):
#     multiplied_list = [element * factor for element in lst]
#     return multiplied_list

# sum_result = find_sum(my_list)
# print(f"Сумма элементов списка: {sum_result}")

# multiplied_result = multiply_list(my_list, 2)
# print(f"Умноженный список: {multiplied_result}")


# def filter_list(lst, condition):
#     filtered_list = [element for element in lst if condition(element)]
#     return filtered_list

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# filtered_result = filter_list(my_list, lambda x: x % 2 == 0)
# print(f"Отфильтрованный список (четные числа): {filtered_result}")

# def remove_duplicates(lst):
#     unique_list = []
#     for element in lst:
#         if element not in unique_list:
#             unique_list.append(element)
#     return unique_list


# my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
# unique_list = remove_duplicates(my_list)
# print(f"Список без повторяющихся чисел: {unique_list}")
# def find_average(lst):
#     average = sum(lst) / len(lst)
#     return average
# average_result = find_average(my_list)
# print(f"Среднее значение списка: {average_result}")

# product-list = []
# while True:
#     new_product = input("введите новый продукт(или 'стоп' для завершения):")
#     if new_product.lower() == 'стоп'
#         break 
#     product_list.append(new_product)
# print('список продуктов:') 
# for product in product_list:
#     print(product)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

def display_menu():
    print("1. Яблоки - $1.00")
    print("2. Бананы - $0.75")
    print("3. Груши - $1.25")
    print("4. Завершить покупки")

def display_cart(cart):
    print("\nВаша корзина:")
    for item in cart.items:
        print(f"{item['product'].name} x {item['quantity']} - ${item['product'].price * item['quantity']:.2f}")
    print(f"\nИтого: ${cart.calculate_total():.2f}")

def main():
    apple = Product("Яблоки", 1.00)
    banana = Product("Бананы", 0.75)
    pear = Product("Груши", 1.25)

    cart = ShoppingCart()

    while True:
        display_menu()
        choice = input("Выберите продукт (1-4): ")

        if choice == "1":
            quantity = int(input("Введите количество яблок: "))
            cart.add_item(apple, quantity)
        elif choice == "2":
            quantity = int(input("Введите количество бананов: "))
            cart.add_item(banana, quantity)
        elif choice == "3":
            quantity = int(input("Введите количество груш: "))
            cart.add_item(pear, quantity)
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

        display_cart(cart)

    total = cart.calculate_total()
    print(f"\nИтого: ${total:.2f}")
    print("Спасибо за покупки!")

if __name__ == "__main__":
    main()


        
