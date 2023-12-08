# ТРП-1-23, Стешин П. А Лаб 3

# 1
print("1 Дано целое число N (> 0). Найти квадрат данного числа, используя для\n"
      "его вычисления следующую формулу: N2 = 1 + 3 + 5 + … + (2*N - 1).\n"
      "После добавления к сумме каждого слагаемого выводить текущее значение суммы\n"
      "(в результате будут выведены квадраты всех целых чисел от 1 до N)")
n = int(input("\tВведите целое число n: "))
n2 = 0
if n > 0:
    for i in range(1, 2*n, 2):
        n2 += i
        print(f"\t{n2}")
else:
    print("\tЧисло должно быть > 0")


# 2
print("2 Дано целое число N (> 0). Найти значение выражения 1.1 – 1.2 + 1.3 – …\n"
      "(N слагаемых, знаки чередуются). Условный оператор не использовать")
n = int(input("\tВведите целое число n: "))
x = 1
summ = 0
for i in range(1, n+1):
    summ += x * (i / 10)
    x *= -1
print(f"\tОтвет: {summ}")


# 3
print("3 Дано целое число N (> 2). Последовательность целых чисел Ak\n"
      "определяется следующим образом: A1 = 1, A2 = 2, A3 = 3, Ak = Ak–1 + Ak–2 – 2·Ak–3,\n"
      "k = 4, 5, … . Вывести элементы A1, A2, …, AN")
n = int(input("\tВведите целое число n: "))
if n>2:
    A = [int(i) for i in range(1, n+1)]
    for K in range(4, n + 1):
        AK = A[K - 1] + A[K - 2] - 2 * A[K - 3]
        A.append(AK)

    for i in range(n):
        print(f"\tA{i + 1} = {A[i]}")


# 4
print("4 Даны целые положительные числа A и B (A < B). Вывести все целые числа\n"
      "от A до B включительно; при этом каждое число должно выводиться\n"
      "столько раз, каково его значение (например, число 3 выводится 3 раза)")
a, b = map(int, input("\tВведите целые положительные числа A и B (A < B): ").split())
if a<b:
    for i in range(a, b+1):
        for j in range(1, i+1):
            print(f"\t{i}")
else:
    print("\tЧисла должны быть A<B")


# 5
print("5 Дано целое число N (> 0). Найти двойной факториал N: N!! = N·(N–2)·(N–4)·…\n"
      "(последний сомножитель равен 2, если N — четное, и 1,если N — нечетное)")
def fac(N):
    if N <= 0:
        return 1
    result = 1
    while N > 1:
        result *= N
        N -= 2
    return result


n = int(input("\tВведите целое число N (> 0): "))

if n > 0:
    result = fac(n)
    print(f"\t{n}!! = {result}")
else:
    print("\tВведите положительное число.")


# 6
print("6 Дано число A (> 1). Вывести наибольшее из целых чисел K, для\n"
      "которых сумма 1 + 1/2 + … + 1/K будет меньше A, и саму эту сумму")
a = float(input("\tВведите число a: "))
if a >= 1:
    K = 1
    summ = 0
    while summ < a:
        K += 1
        summ += 1 / K
    K -= 1
    print(f"\tНаибольшее целое число K: {K}")
    print(f"\tСумма 1 + 1/2 + ... + 1/{K}: {summ}")
else:
    print("\tВведите число A больше 1.")

# 7
print("7 Дано целое число N (> 1). Последовательность чисел Фибоначчи FK\n"
      "определяется следующим образом: F1 = 1, F2 = 1, FK = FK–2 + FK–1, K = 3,\n"
      "4, … . Проверить, является ли число N числом Фибоначчи. Если\n"
      "является, то вывести True, если нет — вывести False")
n = int(input("\tВведите целое число N (> 1): "))
if n >= 1:
      F1, F2 = 1, 1
      while F2 < n:
            F1, F2 = F2, F1 + F2
      if F2 == n:
            print("\tTrue")
      else:
            print("\tFalse")
else:
      print("\tПожалуйста, введите число N больше 1.")


# 8
print("8 Дано целое число N и набор из N вещественных чисел. Вывести в том\n"
      "же порядке округленные значения всех чисел из данного набора (как целые числа),\n"
      "а также сумму всех округленных значений")
n = int(input("\tВведите целое число N: "))
summ = 0
for i in range(n):
    num = float(input("\tВведите вещественное число: "))
    rnum = round(num)
    summ += rnum
    print(f"\tОкругленное значение: {rnum}")
print(f"\tСумма округленных значений: {summ}")


# 9
print("9 Дано целое число N и набор из N целых чисел. Вывести в том же\n"
      "порядке номера всех нечетных чисел из данного набора и количество K\n"
      "таких чисел")
n = int(input("\tВведите целое число N: "))
count = 0
for i in range(1, n + 1):
    num = int(input(f"\tВведите целое число {i}: "))
    if num % 2 != 0:
        count += 1
        print(f"\tНомер нечетного числа: {i}")

print(f"\tКоличество нечетных чисел: {count}")


# 10
print("10 Дано целое число N и набор из N целых чисел, упорядоченный по\n"
      "возрастанию. Данный набор может содержать одинаковые элементы.\n"
      "Вывести в том же порядке все различные элементы данного набора")
n = int(input("\tВведите целое число N: "))
pre = None
for i in range(n):
    num = int(input(f"\tВведите целое число {i + 1}: "))
    if num != pre:
        print(f"\t{num}")
    pre = num


# 11
print("11 Дано целое число N и набор из N целых чисел, содержащий по крайней\n"
      "мере два нуля. Вывести сумму чисел из данного набора,\n"
      "расположенных между последними двумя нулями (если последние нули идут подряд, то вывести 0)")
N = int(input("\tВведите целое число N: "))
l1 = -2
l2 = -1
summ = 0
for i in range(N):
    num = int(input(f"\tВведите целое число {i + 1}: "))
    if num == 0:
        l2 = l1
        l1 = i
    if l2 >= 0 and i > l2 + 1:
        summ += num
print(f"\tСумма чисел между последними двумя нулями: {summ}")


# 12
print("12 Даны целые числа K, N, а также K наборов целых чисел по N элементов\n"
      "в каждом наборе. Для каждого набора вывести номер его первого\n"
      "элемента, равного 2, или число 0, если в данном наборе нет двоек")
K = int(input("\tВведите целое число K: "))
N = int(input("\tВведите целое число N: "))
for k in range(1, K + 1):
    print(f"Набор {k}:")
    found = False
    pos = 1
    while pos <= N:
        num = int(input(f"\tВведите целое число {pos}: "))
        if num == 2:
            found = True
            print(f"\tНомер первой двойки: {pos}")
            break
        pos += 1
    if not found:
        print("\tДвойки нет - 0")

# 13
print("13 Дано целое число N, а также K наборов ненулевых целых чисел.\n"
      "Признаком завершения каждого набора является число 0. Для каждого\n"
      "набора вывести количество его элементов. Вывести также общее\n"
      "количество элементов во всех наборах")
K = int(input("\tВведите целое число K: "))
total_count = 0
for k in range(1, K + 1):
    print(f"\tНабор {k}:")
    count = 1
    num = int(input(f"\tВведите ненулевое целое число (0 - завершение): "))
    while num != 0:
        count += 1
        total_count += 1
        num = int(input(f"\tВведите ненулевое целое число (0 - завершение): "))
    print(f"\tКоличество элементов в наборе {k}: {count}")
    print(f"\tОбщее количество элементов во всех наборах: {total_count}")


# 14
print("14 Дано целое число K, а также K наборов ненулевых целых чисел.\n"
      "Каждый набор содержит не менее двух элементов, признаком его\n"
      "завершения является число 0. Найти количество наборов, элементы\n"
      "которых возрастают.")
K = int(input("\tВведите целое число K: "))
count = 0

for k in range(1, K + 1):
    print(f"\tНабор {k}:")

    num = int(input(f"\tВведите ненулевое целое число: (0 - завершение): "))
    increasing = True
    if num != 0:
        prev_num = num
        while num != 0:
            if num <= prev_num:
                increasing = False
            prev_num = num
            num = int(input(f"\tВведите ненулевое целое число: (0 - завершение): "))
        if increasing:
            count += 1
print(f"\tКоличество наборов с возрастающими элементами: {count}")


# 15
print("15 Дано целое число K, а также K наборов ненулевых целых чисел.\n"
      "Каждый набор содержит не менее двух элементов, признаком его\n"
      "завершения является число 0. Для каждого набора выполнить\n"
      "следующее действие: если элементы набора возрастают, то вывести - 1;\n"
      "если элементы набора убывают, то вывести –1; если элементы набора\n"
      "не возрастают и не убывают, то вывести 0.")
K = int(input("\tВведите целое число K: "))
for k in range(1, K + 1):
    print(f"Набор {k}:")
    num = int(input(f"\tВведите ненулевое целое число (0 - завершение): "))
    res = 0
    if num != 0:
        prev_num = num
        while num != 0:
            num = int(input(f"\tВведите ненулевое целое число (0 - завершение): "))
            if num < prev_num and res >= 0:
                res = -1
            elif num > prev_num and res <= 0:
                res = 1
            prev_num = num
    print(f"\t{res}")

# 16
print("16 Дано целое число N (> 2) и набор из N вещественных чисел. Набор\n"
      "называется пилообразным, если каждый его внутренний элемент либо\n"
      "больше, либо меньше обоих своих соседей (то есть является «зубцом»).\n"
      "Если данный набор является пилообразным, то вывести 0;\n"
      "в противном случае вывести номер первого элемента, не являющегося зубцом")
n = int(input("\tВведите целое число N (>2): "))
if n > 2:
    print("\tВведите набор вещественных чисел:")
    first = float(input("\tВведите 1-е число: "))
    second = float(input("\tВведите 2-е число: "))
    position = 2

    while position < n:
        next_num = float(input(f"\tВведите {position + 1}-е число: "))

        if (second < first and second < next_num) or (second > first and second > next_num):
            position += 1
            first = second
            second = next_num
        else:
            print(f"\t{position}")
            break

    if position == n:
        print("\t0")
else:
    print("\tПожалуйста, введите N больше 2.")


# 17
print("17 Даны целые положительные числа A и B (A < B). Вывести все целые числа от A до B включительно;\n"
      "при этом каждое число должно выводиться столько раз, каково его значение (например, число 3 выводится 3 раза")
a, b = map(int, input("\tВведите целые положительные числа A и B (A < B): ").split())
if a<b:
    for i in range(a, b+1):
        for j in range(1, i+1):
            print(f"\t{i}")
else:
    print("\tЧисла должны быть A<B")


# 18
print("18 Даны целые числа K, N, а также K наборов целых чисел по N элементов "
      "в каждом наборе. Вывести общую сумму всех элементов, входящих в данные наборы")
K = int(input("\tВведите количество наборов K: "))
N = int(input("\tВведите количество элементов в каждом наборе N: "))
summ = 0
for k in range(1, K + 1):
    print(f"Набор {k}:")
    sum1 = 0
    for n in range(1, N + 1):
        num = int(input(f"\tВведите целое число {n}: "))
        sum1 += num
    summ += sum1

print(f"\tОбщая сумма всех элементов в наборах: {summ}")


# 19
print("19 Даны целые числа K, N, а также K наборов целых чисел по N элементов\n"
      "в каждом наборе. Для каждого набора вывести сумму его элементов.")
K = int(input("\tВведите целое число K: "))
N = int(input("\tВведите целое число N: "))

for k in range(1, K + 1):
    print(f"Набор {k}:")
    sum1 = 0
    for n in range(1, N + 1):
        num = int(input(f"\tВведите целое число {n}: "))
        sum1 += num
    print(f"\tСумма элементов набора {k}: {sum1}")


# 20
print("20 Дано целое число K, а также K наборов ненулевых целых чисел. "
      "Каждый набор содержит не менее трех элементов, признаком его "
      "завершения является число 0. Найти количество пилообразных наборов")
K = int(input("\tВведите целое число K: "))
count = 0
for k in range(1, K + 1):
    print(f"\tНабор {k}:")
    first = int(input("\tВведите 1-е целое число (0 - завершение): "))
    second = int(input("\tВведите 2-е целое число (0 - завершение): "))
    pos = 2
    increasing = second > first
    decreasing = second < first

    while second != 0:
        next_num = int(input(f"\tВведите {pos + 1}-е целое число: "))

        if second == next_num:
            increasing = False
            decreasing = False
        elif second < next_num:
            decreasing = False
        elif second > next_num:
            increasing = False

        first = second
        second = next_num
        pos += 1

    if increasing or decreasing:
        count += 1

print(f"\tКоличество пилообразных наборов: {count}")

# Контрольные вопросы по теме «Числа»
# 1. Какие типы чисел Вы знаете в Python
#     Целые, Вещественные, Комплексные, Дробные
# 2. Чем отличаются результаты операций «/» и «//» для целых чисел?
#     «/» - называют деление с плавающей точкой. Это означает, что результат будет вещественным числом
#     «//» - называют целочисленным делением. Результат всегда будет целым числом и если результат не делится нацело,
#     остаток отбрасывается, и результат округляется к наименьшему целому числу
# 3. Какая структура является результатом работы функции divmod()
#     Кортеж, содержащий частное и остаток от деления
# 4. Почему операция вида a<b=c недопустима, а операция вида a<b==c допустима?
#     Операция a<b=c недопустима  из-за правил синтаксиса и приоритета операторов в языке.
#     В этой операции мы сравниваем a с результатом операции b = c, которая присваивает значение c переменной b.
#     В результате оператор = в данном контексте считается оператором присваивания, а не сравнения.
#     Поэтому такая запись вызовет синтаксическую ошибку.
#     Однако операция a < b == c допустима, потому что в этом случае сравниваются значения a, b и c.
#     В данном случае, a сравнивается с b, а затем результат этого сравнения сравнивается с c.
# 5. Назовите основные библиотеки для работы с числами
#     Math, numpy, random
# 6. Назовите известные Вам функции библиотек math
#     sqrt(x), pow(x, y), log(x, base), sin(x), cos(x) и т.д.
# 7. Назовите известные Вам функции библиотек random
#     random(), randint(a, b), shuffle(), randrange(), choice()
# 8. Назовите известные Вам функции библиотек round
#     round(num, 2), round()
# 9. Какими 3 способами можно в Python вычислить значение квадратного корня
#     math.sqrt (144), 144 ** 0.5, pow(144, 0.5)
# 10. Какого типа будет объект после операции деления нацело (//)
#     Целым
# 11. Какого типа будет объект после операции деления (/)
#     Вещественным
# 12. Какого типа будет объект после выполнения операции возведения в степень (**)
#     Целым