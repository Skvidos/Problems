n = int(input())
first = int(str(n)[0])

while first!=1 and n<=10**9:
  n = n * first
  first = int(str(n)[0])
print(n)