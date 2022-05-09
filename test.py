import math

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discriminant = b**2 - 4 * a * c
print('Дискриминант D = %.2f' % discriminant )

if (discriminant > 0) :
  x1 = (-b + math.sqrt(discriminant)) / (2 * a)
  x2 = (-b - math.sqrt(discriminant)) / (2 * a)
  print('x1 = %.2f \nx2 = %.2f' % (x1, x2))
elif (discriminant < 0) :
  x = -b / (2 * a)
  print('x = %.2f' % x)
else:
  print('no')