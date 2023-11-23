# ТРП-1-23, Стешин П. А Лаб 6

# 1
print("Дано целое число N (> 0). Сформировать и вывести целочисленный" +
      "список размера N, содержащий N первых положительных нечетных чисел: 1, 3, 5, … .")
N = int(input("\tВведите число N: "))
num = 1
lst = []
if N > 0:
    for i in range(N):
        list.append(num)
        num += 2
    print(f"\tОтвет: {lst}")
else:
    print("\tN>0")

# 2
print("2 Дано целое число N (> 1), а также первый член A и разность D" +
      "арифметической прогрессии. Сформировать и вывести список размера" +
      "N, содержащий N первых членов данной прогрессии: A, A + D, A + 2·D, A + 3·D, … .")
N = int(input("\tВведите число N: "))
A = int(input("\tВведите первый член A: "))
D = int(input("\tВведите разность D: "))
lst = []
if N > 1:
    for i in range(N):
        res = A + i * D
        lst.append(res)
        print(f"\Ответ: {lst}")
else:
    print("\tN>1")

# 3
print("3 Даны целые числа N (> 2), A и B. Сформировать и вывести " +
      "целочисленный список размера N, первый элемент которого равен A" +
      "второй равен B, а каждый последующий элемент равен сумме всех предыдущих.")
N = int(input("\tВведите число N: "))
A = int(input("\tВведите число A: "))
B = int(input("\tВведите число B: "))
lst = []
if N > 2:
    lst.append(A)
    lst.append(B)
    for i in range(2, N):
        lst.append(sum(lst))
    print(f"\tОтвет: {lst}")
else:
    print("\tN>2")


# 4
print("4 Дан целочисленный список размера N. Вывести все содержащиеся в" +
      "данном списке четные числа в порядке убывания их индексов, а также" +
      "их количество K")
lst = [int(i) for i in input("\tВведите список: ").split()]
lst2 = []
res = ""
for i in range(len(lst)-1, -1, -1):
    if lst[i] % 2 == 0:
        lst2.append(lst[i])
res = " ".join(map(str, lst2))
print(f"\tКоличество четных чисел: {len(lst2)}")
print(f"\tОтвет: {res}")


# 5
print("5 Дан список A ненулевых целых чисел размера 10. Вывести значение" +
      "первого из тех его элементов A[K], которые удовлетворяют неравенству A[K]<A[10]." +
      "Если таких элементов нет, то вывести 0.")
lst = [int(i) for i in input(
    "\tВведите список 10-ти ненулевых целых чисел: ").split() if int(i) > 0]
lst2 = []
res = ""
if len(lst) == 10:
    for i in range(len(lst)):
        if lst[i] < lst[9]:
            lst2.append(lst[i])
        if len(lst2) == 0:
            lst2.append(0)
    res = " ".join(map(str, lst2))
    print(f"\tОтвет: {res}")
else:
    print("\tВведен список =! 10-ти элементов")


# 6
print("6 Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти сумму" +
      "всех элементов списка, кроме элементов с номерами от K до L включительно")
N = int(input("\tВведите размер списка: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
K = int(input("\tВведите число K: "))
L = int(input("\tВведите число L: "))
if len(lst) == N and (1 < K <= L <= N):
    res = sum(lst[:K-1]) + sum(lst[L:])
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список или значения K и L.")


# 7
print("7 Дан целочисленный список размера N. Проверить, чередуются ли внем" +
      "четные и нечетные числа. Если чередуются, то вывести 0, если нет, то" +
      "вывести порядковый номер первого элемента, нарушающего закономерность")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
lst2 = []
flag = bool
res = ''
if len(lst) == N:
    for i in range(1, len(lst)):
        if (lst[i] % 2 == 0 and lst[i-1] % 2 != 0) or (lst[i] % 2 != 0 and lst[i-1] % 2 == 0):
            flag = True
            lst2.append(i)
        else:
            flag = False
            lst2.append(i)
            break
    if flag:
        print(f"\tОтвет: 0")
    else:
        print(f"\tНомер: {len(lst2)+1}")
else:
    print("\tВведен неправильный список.")

# 8
print("8 Дан список A размера N. Найти минимальный элемент " +
      "из его элементов с четными номерами: A[2], A[4], A[6]")
N = int(input("\tВведите размер списка A: "))
A = [int(i) for i in input("\tВведите список: ").split()]
if len(A) == N:
    res = min(A[1::2])
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# 9
print("9 Дан список размера N. Найти номера тех элементов списка, которые" +
      "больше своего правого соседа, и количество таких элементов." +
      "Найденные номера выводить в порядке их возрастания.")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
if len(lst) == N:
    indexes = []
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            indexes.append(i+1)
    res = " ".join(map(str, indexes))
    print(f"\n\tКоличество таких элементов: {len(indexes)}")
    print(f"\tНайденные номера: {res}")
else:
    print("\tВведен неправильный список.")


# 10
print("10 Даны два списка A и B одинакового размера N. Сформировать новый " +
      "список C того же размера, каждый элемент которого равен" +
      "максимальному из элементов списков A и B с тем же индексом.")
N = int(input("\tВведите размер списка N: "))
A = [int(i) for i in input("\tВведите список A: ").split()]
B = [int(i) for i in input("\tВведите список B: ").split()]
C = []
if len(A) == N and len(B) == N:
    for i in range(0, N):
        C.append(max(A[i], B[i]))
    print(f"\tОтвет: {C}")
else:
    print("\tВведен неправильный список.")


# 11
print("11 Дан целочисленный список A размера N. Переписать в новый " +
      "целочисленный список B все четные числа из исходного списка (в том же порядке)" +
      "и вывести размер полученного списка B и его содержимое.")
N = int(input("\tВведите размер списка A: "))
A = [int(i) for i in input("\tВведите список A: ").split()]
B = []
if len(A) == N:
    for i in A:
        if i % 2 == 0:
            B.append(i)
    print(f"\tРазмер списка B: {len(B)}")
    print(f"\tСписок B: {B}")
else:
    print("\tВведен неправильный список.")


# 12
print("12 Дан список A размера N. Сформировать два новых списка B и C: в список B" +
      "записать все положительные элементы списка A, в список C — все отрицательные" +
      "(сохраняя исходный порядок следования элементов)." +
      "Вывести вначале размер и содержимое списка B, а затем — размер и содержимое списка C.")
N = int(input("\tВведите размер списка A: "))
A = [int(i) for i in input("\tВведите список A: ").split()]
B = []
C = []
if len(A) == N:
    for i in A:
        if i > 0:
            B.append(i)
    for i in A:
        if i < 0:
            C.append(i)
    print(f"\tРазмер списка B: {len(B)}, Список B: {B}")
    print(f"\tРазмер списка C: {len(C)}, Список C: {C}")
else:
    print("\tВведен неправильный список.")


# 13
print("13 Дан список A размера N и целое число K (1 ≤ K ≤ N)." +
      "Преобразовать список, увеличив каждый его элемент на исходное значение элемента A[K].")
N = int(input("\tВведите размер списка A: "))
A = [int(i) for i in input("\tВведите список A: ").split()]
K = int(input("\tВведите целое число K: "))
lst = []
res = ""
if len(A) == N and (1 <= K <= N):
    for i in range(0, N):
        lst.append(A[i] + A[K - 1])
    res = " ".join(map(str, lst))
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# 14
print("Дан список размера N. Поменять местами его минимальный и максимальный элементы.")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
if len(lst) == N:
    max_num = max(lst)
    min_num = min(lst)
    lst[lst.index(max_num)] = min_num
    lst[lst.index(min_num)] = max_num
    print(f"\tОтвет: {lst}")
else:
    print("\tВведен неправильный список.")


# 15
print("15 Дан список размера N (N — четное число). Поменять местами его " +
      "первый элемент со вторым, третий — с четвертым и т. д.")
N = int(input("\tВведите размер списка N (N — четное число): "))
lst = [int(i) for i in input("\tВведите список: ").split()]
res = ""
if len(lst) == N and N % 2 == 0:
    for i in range(0, N, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    res = " ".join(map(str, lst))
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# 16
print("16 Дан список размера N. Обнулить элементы списка, расположенные" +
      "между его минимальным и максимальным элементами (не включая минимальный и максимальный элементы).")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
res = ""
if len(lst) == N:
    max_num = max(lst)
    min_num = min(lst)
    for i in range(lst.index(min_num) + 1, lst.index(max_num)):
        lst[i] = 0
    for i in range(lst.index(min_num) - 1, lst.index(max_num), -1):
        lst[i] = 0
    res = " ".join(map(str, lst))
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# 17
print("17 Дан список размера N и целое число K (1 ≤ K ≤ N)." +
      "Удалить из списка элемент с порядковым номером K")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
K = int(input("\tВведите целое число K: "))
res = ""
if len(lst) == N and (1 <= K <= N):
    lst.pop(K - 1)
    res = " ".join(map(str, lst))
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# 18
print("18 Дан список размера N и целые числа K и L (1 ≤ K < L ≤ N)." +
      "Удалить из списка элементы с номерами от K до L включительно " +
      "и вывести размер полученного списка и его содержимое.")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
K = int(input("\tВведите целое число K: "))
L = int(input("\tВведите целое число L: "))
res = ""
if len(lst) == N and (1 <= K < L <= N):
    lst = lst[:K - 1] + lst[L:]
    res = " ".join(map(str, lst))
    print(f"\tРазмер списка: {len(lst)}")
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# 19
print("19 Дан целочисленный список размера N. Удалить из списка все нечетные числа" +
      "и вывести размер полученного списка и его содержимое.")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
res = ""
if len(lst) == N:
    lst = [int(i) for i in lst if i % 2 == 0]
    res = " ".join(map(str, lst))
    print(f"\tРазмер списка: {len(lst)}, список: {res}")
else:
    print("\tВведен неправильный список.")


# 20
print("20 Дан целочисленный список размера N. Удалить из списка все " +
      "соседние одинаковые элементы, оставив их первые вхождения.")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
res = ""
if len(lst) == N:
    lst = set(lst)
    res = " ".join(map(str, lst))
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# Домашняя работа
# 1
print("1 Дан целочисленный список размера N. Вывести все содержащиеся в данном списке" +
      "нечетные числа в порядке возрастания их индексов, а также их количество K")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
res = ""
if len(lst) == N:
    indexes = []
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            indexes.append(i+1)
    res = " ".join(map(str, indexes))
    print(f"\n\tКоличество таких элементов: {len(indexes)}, Индексы: {res}")
else:
    print("\tВведен неправильный список.")

# 2
print("2 Дан список A размера N (N — четное число). Вывести его элементы с " +
      "четными номерами в порядке возрастания номеров: A2, A4, A6, …, AN." +
      "Условный оператор не использовать.")
N = int(input("\tВведите размер списка A: "))
A = [int(i) for i in input("\tВведите список A: ").split()]
lst = []
res = ""
if len(A) == N:
    lst.append(A[1::2])
    res = " ".join(map(str, lst))
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# 3
print("3 Дан список размера N и целые числа K и L (1 ≤ K ≤ L ≤ N). " +
      "Найти сумму элементов списка с номерами от K до L включительно.")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
K = int(input("\tВведите K: "))
L = int(input("\tВведите L: "))
if len(lst) == N and (1 <= K <= L <= N):
    res = sum(lst[K-1:L])
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# 4
print("4 Дан список размера N. Найти номер его первого локального минимума" +
      "(локальный минимум — это элемент, который меньше любого из своих соседей).")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
if len(lst) == N:
    res = lst.index(min(lst)) + 1
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# 5
print("5 Дан целочисленный список A размера N. Переписать в новый целочисленный список B " +
      "того же размера вначале все элементы исходного списка с четными номерами, " +
      "а затем — с нечетными: A[2],A[4],A[6], …, A[1], A[3], A[5], … . Условный оператор не использовать")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
B = []
res = ""
if len(lst) == N:
    for i in range(len(lst)):
        if i % 2 == 0:
            B.append(lst[i])
    for i in range(len(lst)):
        if i % 2 != 0:
            B.append(lst[i])
    res = " ".join(map(str, B))
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# 6
print("6 Даны два списка A и B размера 5, элементы которых упорядочены по возрастанию." +
      "Объединить эти списки так, чтобы результирующий список C (размера 10) остался упорядоченным повозрастанию.")
A = [int(i) for i in input("\tВведите список A: ").split()]
B = [int(i) for i in input("\tВведите список B: ").split()]
C = []
res = ""
if len(A) == 5 and len(B) == 5:
    C = A + B
    C.sort()
    res = " ".join(map(str, C))
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")

# 7
print("7 Дан список размера N. Осуществить сдвиг элементов списка влево на " +
      "одну позицию (при этом A[N] перейдет в A[N–1], A[N–1] — в A[N–2], …, A[2] в A[1], a " +
      "исходное значение первого элемента будет потеряно). Последний элемент полученного списка положить равным 0.")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
res = ""
if len(lst) == N:
    lst[:-1] = lst[1:]
    lst[-1] = 0
    res = " ".join(map(str, lst))
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# Задание повышенной сложности на списки (для самоконтроля полученных з наний)
# 1
print("1 Дан целочисленный список размера N. Найти максимальное" +
      "количество его одинаковых элементов")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
lst2 = []
if len(lst) == N:
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            lst2.append(lst[i])
    print(f"\tМаксимальное количество одинаковых элементов: {len(lst2)}")
else:
    print("\tВведен неправильный список.")

# 2
print("2 Дан список размера N (N — четное число). " +
      "Поменять местами первую и вторую половины списка.")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
lst2 = []
if len(lst) == N:
    fst_part = lst[:len(lst)//2]
    del lst[:len(lst)//2]
    sec_part = lst
    lst2 = sec_part + fst_part
    res = " ".join(map(str, lst2))
    print(f"\tОтвет: {res}")
else:
    print("\tВведен неправильный список.")


# 3
print("3 Дан список A размера N и целое число K (1 ≤ K ≤ 4, K < N). " +
      "Осуществить циклический сдвиг элементов списка вправо на K позиций " +
      "(при этом A[1] перейдет в A[K+1], A[2] — в A[K+2], …, A[N] — в A[K]). " +
      "Допускается использовать вспомогательный список из 4 элементов.")
N = int(input("\tВведите размер списка A: "))
K = int(input("\tВведите число K: "))
A = [int(i) for i in input("\tВведите список: ").split()]
if len(A) == N and (1 <= K <= 4 and K < N):
    B = A[N-K:] + A[:N-K]
    res = " ".join(map(str, B))
    print(f"\t{res}")
else:
    print("\tВведен неправильный список.")


# 4
print("4 Дан целочисленный список размера N. Удалить из списка все " +
      "элементы, встречающиеся менее трех раз, и вывести размер" +
      "полученного списка и его содержимое.")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
lst2 = []
res = ""
if len(lst) == N:
    for i in lst:
        if lst.count(i) < 3:
            lst2.append(i)
    res = " ".join(map(str, lst2))
    print(f"\t{res}")
else:
    print("\tВведен неправильный список.")


# 5
print("5 Дан целочисленный список размера N. Удалить из списка все" +
      "одинаковые элементы, оставив их последние вхождения.")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
lst2 = []
res = ""
if len(lst) == N:
    for i in lst:
        if lst.count(i) == 1:
            lst2.append(i)
    res = " ".join(map(str, lst2))
    print(f"\t{res}")
else:
    print("\tВведен неправильный список.")


# 6
print("6 Дан целочисленный список размера N. Удалить из списка все элементы, " +
      "встречающиеся ровно два раза, и вывести размер полученного списка и его содержимое")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
lst2 = []
res = ""
if len(lst) == N:
    for i in lst:
        if lst.count(i) != 2:
            lst2.append(i)
    res = " ".join(map(str, lst2))
    print(f"\tРазмер списка: {len(lst2)}, список: {res}")
else:
    print("\tВведен неправильный список.")


# 7
print("7 Дан список размера N. Вставить элемент с нулевым значением перед" +
      "минимальным и после максимального элемента списка.")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
if len(lst) == N:
    lst.insert(lst.index(min(lst))+1, lst[0])
    lst.insert(lst.index(max(lst))+1, lst[0])
    res = " ".join(map(str, lst))
    print(f"\tСписок: {res}")
else:
    print("\tВведен неправильный список.")


# 8
print("8 Дан список размера N. Продублировать в нем элементы с четными номерами (2, 4, …)." +
      "Условный оператор не использовать.")
N = int(input("\tВведите размер списка N: "))
lst = [int(i) for i in input("\tВведите список: ").split()]
if len(lst) == N:
    for i in range(1, len(lst), 2):
        lst.insert(i, lst[i])
    res = " ".join(map(str, lst))
    print(f"\tСписок: {res}")
else:
    print("\tВведен неправильный список.")


# 9
print("9 Дан целочисленный список A размера N. Назовем серией группу подряд" +
      "идущих одинаковых элементов, а длиной серии — количество этих" +
      "элементов (длина серии может быть равна 1). Сформировать два новых" +
      "целочисленных списка B и C одинакового размера, записав в список B" +
      "длины всех серий исходного списка, а в список C — значения" +
      "элементов, образующих эти серии.")
N = int(input("\tВведите размер списка A: "))
A = [int(i) for i in input("\tВведите список A: ").split()]
B = []
C = []
len = 1
pre = A[0]

for i in range(1, N):
    if A[i] == pre:
        len += 1
    else:
        B.append(len)
        C.append(pre)
        len = 1
        pre = A[i]

B.append(len)
C.append(pre)
print(f"\tB: {B}")
print(f"\tC: {C}")
