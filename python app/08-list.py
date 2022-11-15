
bicycles = ['trek','readline','apple','iPhone']
print(bicycles)
print(bicycles[0])
print(bicycles[3])

print(bicycles[0].title())

bicycles[0]='R'
print(bicycles)

bicycles.append('trek')
print(bicycles)

bicycles.insert(0,'Alina')
print(bicycles)

del bicycles[0]
print(bicycles)

name_bicycles = bicycles.pop()
print(bicycles)
print(name_bicycles)

name1_bicycles = bicycles.pop(0)
print(name1_bicycles)

bicycles.remove('apple')
print(bicycles)

bicycles = ['trek','readline','apple','iPhone']
print(bicycles)

bicycles.sort()
print(bicycles)

bicycles.sort(reverse=True)
print(bicycles)
print('-------------------------')
bicycles = ['trek','readline','apple','iPhone']
print(bicycles)
print(sorted(bicycles))
print(bicycles)
print(len(bicycles))