#---1

# n = int(input('Введите трехзначное число: '))

# d1 = n % 10
# n = n // 10

# d2 = n % 10
# n = n // 10

# print('Сумма цифр числа:', n + d1 + d2)


#---2

# n = input('Введите трехзначное число: ')

# a = int(n[0])
# b = int(n[1])
# c = int(n[2])

# print('Сумма цифр числа:', a + b + c)


#---3 Random

# from random import random

# n = random() * 900 + 100

# n = int(n)
# print(n)

# a = n // 100
# b = (n // 10) % 10
# c = n % 10

# print(a + b + c)


#---4

n = input('Введите трехзначное число: ')

n = int(n)
print(n)

a = n // 100
b = (n // 10) % 10
c = n % 10

print(a + b + c)