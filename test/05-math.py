
print(2+2)

print(3-2)

print(2*3)

print(2/3)

print(2**3)

print(3**3)

print(1+2*3)

print((1+2)*3)

digits = [1,2,3,4,5,6,7,8,9,10,11]
print(min(digits),max(digits),sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)

digits = [1,2,3,4,5,6,7,8,9,10,11]
print(digits[0:3])
print(digits[:2])
print(digits[1:5])
print(digits[-3:])
for digit in digits[-3:]:
    print(digit)

digits = [1,2,3,4,5,6,7,8,9,10,11]
digits2 = digits[:]
print("-----------------------")
print(digits)
print(digits2)
digits.append(33)
digits2.append(66)
print("-----------------------")
print(digits)
print(digits2)