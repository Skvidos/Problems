import math

AB = float(input('Длина первого катета: '))
AC = float(input('Длина второго катета: '))

BC = math.sqrt(AB**2 + AC**2)

S = (AB * AC) / 2
P = AB + AC + BC

print('Площадь теругольника: %.2f' % S)
print('Периметр теругольника: %.2f' % P)