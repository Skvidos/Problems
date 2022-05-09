n, m = map(int, input().split())
mas1 = []
for i in range(n):
  row = list(map(int, input().split()))
  mas1.append(row)
input()
mas2 = []
for i in range(n):
  row = list(map(int, input().split()))
  mas2.append(row)
for i in range(n):
  for j in range(m):
    print(mas1[i][j] + mas2[i][j], end=' ')
  print()