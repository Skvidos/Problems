n1 = int(input('Первое: '))
n2 = int(input('Второе: '))

bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2

print('OR: %s' % bin(bit_or))
print('AND: %s' % bin(bit_and))
print('XOR: %s' % bin(bit_xor))