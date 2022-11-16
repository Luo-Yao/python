
# sum 1+2+3+...100
sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)

print("-------------------")

# 1*2*2*...100
acc = 1
n = 1
while n <= 100:
    acc = acc * n
    n = n + 1
print(acc)