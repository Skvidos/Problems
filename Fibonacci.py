fib1 = fib2 = 1

n = int(input('Number: '))
n -= 2

while n > 0:
  fib1, fib2 = fib2, fib1 + fib2
  n -= 1

print('Значение этого элемента:', fib2)