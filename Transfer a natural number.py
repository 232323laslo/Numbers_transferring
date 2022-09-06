n = int(input('Your number: '))

bin_num = bin(n)
oct_num = oct(n)
hex_num = hex(n)

print(bin_num[2:].upper())
print(oct_num[2:].upper())
print(hex_num[2:].upper())