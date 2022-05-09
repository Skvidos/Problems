n = int(input())
i = 0

while 2**i<n:
  # print(2**i, i)
  i += 1
# print(2**i, i)
if 2**i==n:
  print(i)
else: 
  print('no')