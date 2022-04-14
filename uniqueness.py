from random import random

N = 10
arr = [0] * N
for i in range(N):
  arr[i] = int(random() * 50)
print(arr)

for i in range (N-1):
  for j in range(i+1, N):
    if arr[i] == arr[j]:
      print('Есть одинаковые', arr[i], arr[j])
      quit()
print('Все уникальные')