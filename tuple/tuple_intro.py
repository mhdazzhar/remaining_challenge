fruits=("apple","banana","dragonfruit","orange")
print(fruits)
print(type(fruits))

y=list(fruits)
print(y)
print(type(y))
y.insert(2,"mango")
print(y)
y.remove(y[2])
print(y)
print(len(y))
