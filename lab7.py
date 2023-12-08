# ТРП-1-23, Стешин П. А Лаб 7

# 1
import random
print(
    "1. Даны целые положительные числа M и N. Сформировать целочисленную матрицу размера M × N, у которой все элементы I - й строки имеют значение 10*I (I = 1, …, M)")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
l = [0]*N
print("\tМатрица:")
for i in range(1, M+1):
    for j in range(N):
        l[j] = 10*i
    res = "\t".join(map(str, l))
    print("\t" + res)


# 2
print("2. Даны целые положительные числа M и N. Сформировать целочисленную матрицу размера M × N, у которой все элементы J - го столбца имеют значение 5*J (J = 1, …, N)")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
l = [0]*N
print("\tМатрица:")
for i in range(M):
    for j in range(N):
        l[j] = 5*(j+1)
    res = "\t".join(map(str, l))
    print("\t" + res)


# 3
print("3. Даны целые положительные числа M, N, число D и набор из M чисел. "
      "Сформировать матрицу размера M × N, у которой первый столбец совпадает с исходным набором чисел, "
      "а элементы каждого следующего столбца равны сумме соответствующего элемента предыдущего столбца и числа D "
      "(в результате каждая строка матрицы будет содержать элементы арифметической прогрессии)")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
D = random.randrange(0, 50)
numbers = [int(i) for i in range(1, M+1)]
matrix = []
print("\tМатрица:")
print(f"\tD = {D}")
for i in range(M):
    row = []
    for j in range(N):
        if j == 0:
            row.append(numbers[i])
        else:
            previous_element = row[j-1]
            current_element = previous_element + D
            row.append(current_element)
    matrix.append(row)

for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)


# 4
print("4 Дана матрица размера M × N и целое число K (1 ≤ K ≤ M). Вывести элементы K-й строки данной матрицы.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
K = random.randrange(1, M)
matrix = []
print("\tМатрица:")
print(f"\tK = {K}")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
res2 = " ".join(map(str, matrix[K-1]))
print(f"\tЭлементы {K} строки: {res2}")


# 5
print("5 Дана матрица размера M × N и целое число K (1 ≤ K ≤ N). Вывести элементы K-го столбца данной матрицы")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
K = random.randrange(1, N)
matrix = []
elements = []
print("\tМатрица:")
print(f"\tK = {K}")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    elements.append(row[K-1])
    res = "\t".join(map(str, row))
    print("\t" + res)
res2 = " ".join(map(str, elements))
print(f"\tЭлементы {K} столбца: {res2}")


# 6
print("6 Дана матрица размера M × N. Вывести ее элементы, расположенные в строках с четными номерами (2, 4, …). "
      "Вывод элементов производить по строкам, условный оператор не использовать")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
print(f"\tЭлементы с четными номерами:")
for row in matrix[1::2]:
    res = "\t".join(map(str, row))
    print("\t" + res)


# 7
print("7 Дана матрица размера M × N. Вывести ее элементы, расположенные в столбцах с нечетными номерами (1, 3, …). "
      "Вывод элементов производить по столбцам, условный оператор не использовать.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
print(f"\tЭлементы с нечетными номерами:")
print("\t", end="")
for column_index in range(1, len(matrix[0]), 2):
    for row in matrix:
        print(row[column_index], end=" ",)

# 8
print("8 Дана матрица размера M × N и целое число K (1 ≤ K ≤ M). "
      "Найти сумму и произведение элементов K-й строки данной матрицы.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
K = random.randrange(1, M)
matrix = []
summ = 0
prod = 1
print(f"\tK = {K}")
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for i in matrix[K-1]:
    summ += i
    prod *= i
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
print(f"\tСумма элементов {K} строки: {summ}")
print(f"\tПроизведение элементов {K} строки: {prod}")


# 9
print("9. Дана матрица размера M × N и целое число K (1 ≤ K ≤ N)."
      "Найти сумму и произведение элементов K-го столбца данной матрицы.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
K = random.randrange(1, M)
matrix = []
summ = 0
prod = 1
print(f"\tK = {K}")
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    summ += row[K-1]
    prod *= row[K-1]
    res = "\t".join(map(str, row))
    print("\t" + res)
print(f"\tСумма элементов {K} столбца: {summ}")
print(f"\tПроизведение элементов {K} столбца: {prod}")


# 10
print("10. Дана матрица размера M × N. В каждой строке матрицы найти минимальный элемент.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
minn = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
    minn += [min(row)]
res2 = " ".join(map(str, minn))
print(f"\tМинимальные элементы: {res2}")

# 11
print("11. Дана матрица размера M × N. В каждом столбце матрицы найти максимальный элемент.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
maxx = []
print("\tМатрица:")

for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for j in range(len(matrix[0])):
    column = [matrix[i][j] for i in range(len(matrix))]
    max_element = max(column)
    maxx.append(max_element)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
res2 = " ".join(map(str, maxx))
print(f"\tМаксимальные элементы: {res2}")


# 12
print("12 Дана матрица размера M × N. Найти максимальный среди минимальных элементов ее строк.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
minn = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
    minn += [min(row)]
maxx = max(minn)
print(f"\tМаксимальный среди минимальных элементов: {maxx}")


# 13
print("13 Дана матрица размера M × N и целые числа K1 и K2 (1 ≤ K1 < K2 ≤ M). "
      "Поменять местами строки матрицы с номерами K1 и K2.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
K1 = int(input("\tВведите целое число K1: "))
K2 = int(input("\tВведите целое число K2: "))
matrix = []
if (1 <= K1 < K2 <= M):
    print("\tМатрица:")
    for i in range(M):
        row = []
        for j in range(N):
            row.append(random.randrange(0, 50))
        matrix.append(row)
    for row in matrix:
        res = "\t".join(map(str, row))
        print("\t" + res)
    print("\tПреобразование матрицы:")
    matrix[K1-1], matrix[K2-1] = matrix[K2-1], matrix[K1-1]
    for row in matrix:
        res = "\t".join(map(str, row))
        print("\t" + res)
else:
    print("\tЧисла должны быть 1 ≤ K1 < K2 ≤ M")


# 14
print("14. Дана матрица размера M × N и целые числа K1 и K2 (1 ≤ K1 < K2 ≤ N). "
      "Поменять местами столбцы матрицы с номерами K1 и K2.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
K1 = int(input("\tВведите целое число K1: "))
K2 = int(input("\tВведите целое число K2: "))
matrix = []
if (1 <= K1 < K2 <= N):
    print("\tМатрица:")
    for i in range(M):
        row = []
        for j in range(N):
            row.append(random.randrange(0, 50))
        matrix.append(row)
    for row in matrix:
        res = "\t".join(map(str, row))
        print("\t" + res)
    print("\tПреобразование матрицы:")
    for i in range(M):
        matrix[i][K1-1], matrix[i][K2-1] = matrix[i][K2-1], matrix[i][K1-1]
    for row in matrix:
        res = "\t".join(map(str, row))
        print("\t" + res)
else:
    print("\tЧисла должны быть 1 ≤ K1 < K2 ≤ N")


# 15
print("15. Дана матрица размера M × N. "
      "Преобразовать матрицу, поменяв местами минимальный и максимальный элемент в каждой строке.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
print("\tПреобразвание матрицы:")
for row in matrix:
    min_val = min(row)
    max_val = max(row)
    min_index = row.index(min_val)
    max_index = row.index(max_val)
    row[min_index], row[max_index] = row[max_index], row[min_index]
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)


# 16
print("16 Дана матрица размера M × N. "
      "Преобразовать матрицу, поменяв местами минимальный и максимальный элемент в каждом столбце.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
print("\tПреобразование матрицы:")
for col in range(len(matrix[0])):
    column = [matrix[row][col] for row in range(len(matrix))]
    min_val = min(column)
    max_val = max(column)
    min_index = column.index(min_val)
    max_index = column.index(max_val)
    matrix[min_index][col], matrix[max_index][col] = matrix[max_index][col], matrix[min_index][col]
for row in matrix:
    res2 = '\t'.join(map(str, row))
    print("\t" + res2)


# 17
print("17 Дана квадратная матрица A порядка M. Найти сумму элементов ее главной диагонали, "
      "то есть диагонали,содержащей следующие элементы: A1,1, A2,2, A3,3, …, AM,M.")
M = int(input("\tВведите целое положительное число M: "))
matrix = []
elemets = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(M):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
for i in range(M):
    for j in range(M):
        if i == j:
            elemets.append(matrix[i][j])
print(f"\tСумма элементов главной диагонали: {sum(elemets)}")


# 18
print("18 Дана квадратная матрица A порядка M. "
      "Найти среднее арифметическое элементов ее побочной диагонали, "
      "то есть диагонали, содержащей следующие элементы: A1,M, A2,M–1, A3,M–2, …,AM,1")
M = int(input("\tВведите целое положительное число M: "))
matrix = []
elemets = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(M):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
total_sum = 0
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i + j == len(matrix) - 1:
            total_sum += matrix[i][j]
            count += 1
    average = total_sum / count
print(
    f"\tСреднее арифметическое элементов побочной диагонали: {average}")


# 19
print("19 Дана квадратная матрица A порядка M. Найти сумму элементов каждой ее диагонали, "
      "параллельной главной(начиная с одноэлементной диагонали A1,M).")
M = int(input("\tВведите целое положительное число M: "))
matrix = []
elemets = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(M):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
for k in range(M):
    sum_diag = 0
    for i in range(k + 1):
        sum_diag += matrix[i][k - i]
    elemets.append(sum_diag)
for l in range(1, M):
    sum_diag = 0
    for i in range(l, M):
        sum_diag += matrix[i][i - l]
    elemets.append(sum_diag)

print(f"\tСумма элементов каждой диагонали: {sum(elemets)}")

# 20
print("20 Дана квадратная матрица A порядка M. Найти минимальный элемент для каждой ее диагонали, "
      "параллельной главной (начиная содноэлементной диагонали A1,M).")
M = int(input("\tВведите целое положительное число M: "))
matrix = []
elemets = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(M):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
for k in range(M):
    min_diag = matrix[k][k]
    for i in range(k + 1):
        if matrix[i][k - i] < min_diag:
            min_diag = matrix[i][k - i]
    elemets.append(min_diag)
for l in range(1, M):
    min_diag = matrix[l][l]
    for i in range(l, M):
        if matrix[i][i - l] < min_diag:
            min_diag = matrix[i][i - l]
    elemets.append(min_diag)

print(f"\tМинимальные элементы диагонали: {min(elemets)}")


# Дополнительные задания повышенной сложности
# 1
print("1 Треугольник Паскаля. Вывести на экран треугольник Паскаля из n строк. "
      "Придумать структуру данных для хранения треугольника Паскаля "
      "(например, стандартная матрица, что, однако, не экономно)."
      "Реализовать показ треугольника по данным из этой структуры.")
n = int(input("\tВведите целое положительное число n: "))
triangle = []

for i in range(n):
    row = [1]
    if triangle:
        last_row = triangle[-1]
        row.extend([last_row[j] + last_row[j + 1]
                    for j in range(len(last_row) - 1)])
        row.append(1)
    triangle.append(row)

width = len(" ".join(map(str, triangle[-1])))
for row in triangle:
    print(" ".join(map(str, row)).center(width))


# 2
print("2 Дана целочисленная матрица размера M × N. "
      "Найти элемент, являющийся максимальным в своей строке и минимальным в своем столбце. "
      "Если такой элемент отсутствует, то вывести 0.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)


def element(matrix):
    max_in_rows = []
    min_in_cols = []
    column = []
    for row in matrix:
        max_in_rows.append(max(row))
    for col in range(len(matrix[0])):
        column = [matrix[row][col] for row in range(len(matrix))]
        min_in_cols.append(min(column))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == max_in_rows[i] == min_in_cols[j]:
                return matrix[i][j]
    return 0


print(f"\t{element(matrix)}")


# 3
print("3. Дана целочисленная матрица размера M × N. Найти номер последней из ее строк, "
      "содержащих только четные числа. Если таких строк нет, то вывести 0")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)


def element(matrix):
    for i in range(len(matrix) - 1, -1, -1):
        if all(number % 2 == 0 for number in matrix[i]):
            return i + 1
    return 0


print(f"\t{element(matrix)}")

# 4
print("4 Дана целочисленная матрица размера M × N. Найти количество ее строк, все элементы которых различны")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)

count = 0
for row in matrix:
    if len(row) == len(set(row)):
        count += 1
print(f"\tКоличество строк, все элементы которых различны: {count}")


# 5
print("5 Дана матрица размера M × N. Поменять местами строки, "
      "содержащие минимальный и максимальный элементы матрицы.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)

print("Получим:")

min_val = max_val = matrix[0][0]
min_pos = max_pos = (0, 0)

for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        if val < min_val:
            min_val, min_pos = val, (i, j)
        elif val > max_val:
            max_val, max_pos = val, (i, j)

if min_pos[0] != max_pos[0]:
    matrix[min_pos[0]], matrix[max_pos[0]
                               ] = matrix[max_pos[0]], matrix[min_pos[0]]

for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)


# 6
print("6 Дана матрица размера M × N. Поменять местами столбцы,"
      "содержащие минимальный и максимальный элементы матрицы.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)


def swap_columns(matrix):
    min_val = max_val = matrix[0][0]
    min_col = max_col = 0

    for row in matrix:
        for col_index, element in enumerate(row):
            if element < min_val:
                min_val, min_col = element, col_index
            elif element > max_val:
                max_val, max_col = element, col_index

    if min_col != max_col:
        for row in matrix:
            row[min_col], row[max_col] = row[max_col], row[min_col]

    return matrix


matrix = swap_columns(matrix)
print("\tПолучим:")
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)


# 7
print("7. Дана матрица размера M × N. Упорядочить ее строки так, чтобы их первые элементы "
      "образовывали возрастающую последовательность.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)

print("\tПолучим:")

for row in matrix:
    sorted_matrix = sorted(row)
    res = "\t".join(map(str, sorted_matrix))
    print("\t" + res)


# 8
print("8 Дана матрица размера M × N. Упорядочить ее столбцы так, "
      "чтобы их последние элементы образовывали убывающую последовательность.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
matrix = []
matrix2 = []
matrix3 = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)

print("\tПолучим:")

for j in range(len(matrix[0])):
    column = [matrix[i][j] for i in range(len(matrix))]
    sorted_column = sorted(column, reverse=True)
    matrix2 += [sorted_column]
for k in range(len(matrix2[0])):
    rows = [matrix2[l][k] for l in range(len(matrix2))]
    matrix3 += [rows]
for row in matrix3:
    res2 = '\t'.join(map(str, row))
    print("\t" + res2)


# 9
print("9 Дана матрица размера M × N и целое число K (1 ≤ K ≤ M). "
      "Перед строкой матрицы с номером K вставить строку из нулей.")
M, N = map(int, input("\tВведите целые положительные числа M и N: ").split())
K = random.randrange(1, M)
matrix = []
print("\tМатрица:")
print(f"\tK = {K}")
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
print("\tПолучим:")
row_z = [0] * len(matrix[0])
matrix.insert(K-1, row_z)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)


# 10
print("10 Дана квадратная матрица порядка M. Обнулить элементы матрицы, "
      "лежащие ниже главной диагонали. Условный оператор не использовать.")
M = int(input("\tВведите целое положительное число M: "))
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(M):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)

print("\tПолучим:")

for i in range(1, len(matrix)):
    for j in range(i):
        matrix[i][j] = 0

for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)

# 11
print("11 Дана квадратная матрица порядка M. Обнулить элементы матрицы,"
      "лежащие одновременно выше главной диагонали и выше побочной"
      "диагонали. Условный оператор не использовать.")
M = int(input("\tВведите целое положительное число M: "))
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(M):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)

print("\tПолучим:")

for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        matrix[i][j] = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j] *= i + j >= len(matrix) - 1

for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)

# 12
print("12 Дана квадратная матрица A порядка M. Зеркально отразить ее элементы относительно главной диагонали "
      "(при этом элементы главной диагонали останутся на прежнем месте, элемент A1,2 "
      "поменяется местами с A2,1, элемент A1,3 — с A3,1 и т. д.). Вспомогательную матрицу не использовать.")
M = int(input("\tВведите целое положительное число M: "))
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(M):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)
print("\tПолучим:")

for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)


# 13
print("13 Дана квадратная матрица A порядка M. Повернуть ее на угол 90° в "
      "положительном направлении, то есть против часовой стрелки "
      "(при этом элемент A1,1 перейдет в AM,1, элемент AM,1 — в AM,M и т. д.). "
      "Вспомогательную матрицу не использовать.")
M = int(input("\tВведите целое положительное число M: "))
matrix = []
print("\tМатрица:")
for i in range(M):
    row = []
    for j in range(M):
        row.append(random.randrange(0, 50))
    matrix.append(row)
for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)

print("\tПолучим:")

for i in range(len(matrix)):
    for j in range(i, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

matrix.reverse()

for row in matrix:
    res = "\t".join(map(str, row))
    print("\t" + res)


# Контрольные вопросы по теме "списки"
# 1   К какому базовому типу относятся списки (изменяемый \ не
# изменяемый, последовательности / не последовательности), раскройте
# данные положения на примерах.
#
#     Списки относятся к изменяемым, последовательностям типам. Например в Python мы можем
# изменять элементы списка с помощи индексации:
#     my_list = [1, 2, 3]
#     my_list[0] = 10
#     print(my_list)  Вывод: [10, 2, 3]

#     Чтобы проверить, является ли список последовательным, мы можем сравнить их элементы.
# Если элементы обоих списков равны, то список является последовательным.
#     list1 = [1, 2, 3]
#     list2 = [1, 2, 3]
#     list3 = [3, 2, 1]

#     if list1 == list2:
#         print("Список 1 и список 2 совпадают")
#     else:
#         print("Список 1 и список 2 не совпадают")

#     if list1 == list3:
#         print("Список 1 и список 3 совпадают")
#     else:
#         print("Список 1 и список 3 не совпадают")

#     Вывод будет такой:
#     Список 1 и список 2 совпадают
#     Список 1 и список 3 не совпадают

# 2   Объясните как работают методы списков: s.append(x), s.count(x), s.index(x),
# s.insert(i,j), s.remove(x), s.reverse(), s.sort()

# s.append(x) - Добавляет элемент в конец списка.
# s.count(x) - Возвращает количество элементов в списке.
# s.index(x) - Возвращает индекс первого вхождения элемента в списке.
# s.insert(i, j) - Вставляет элемент j в позицию i.
# s.remove(x) - Удаляет первое вхождение элемента x из списка.
# s.reverse() - Переворачивает список.
# s.sort() - Сортирует список.

# 3   Покажите, как на языке Python объявляется одномерный список и заполняется N
# количеством нулевых элементов.
# N = 10
# my_list = [0] * N
# print(my_list)
# Вывод: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 4   Покажите, как на языке Python объявляется двумерный список и заполняется N*M
# количеством нулевых элементов.
# N = 3
# M = 4
# matrix = [[0] * M for _ in range(N)]
# print(matrix)
# Вывод: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# 5   Назовите четыре операции, которые изменяют непосредственно объект списка.
# s.append(x) - Добавляет элемент в конец списка.
# s.insert(i, j) - Вставляет элемент j в позицию i.
# s.remove(x) - Удаляет первое вхождение элемента x из списка.
# s.pop(i) - Удаляет элемент на указанной позиции в списке и возвращает его значение.
# Если индекс не указан, то удаляется и возвращается последний элемент списка.
