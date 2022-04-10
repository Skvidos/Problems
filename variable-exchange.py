a = 5
b = 7

buf = a
a = b
b = buf

a = 5
b = 7
a = a + b # 12
b = a - b # 12-7=5
a = a - b # 12-5=7

print(a, b)