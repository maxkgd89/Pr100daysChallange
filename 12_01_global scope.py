print("local scope X")
x = 10
def increase(x):
  x += 1
  print(x)
increase(x)
print(x)

print("global scope Y")
y = 10
def increase2(): # can not use as def increase2(y)
  global y
  y += 1
  print(y)
increase2() # can not call as increase2(y)
print(y)

print("different way to use global scope Z")
z=10
def increase3(z):
  print(z)
  return z + 1
print(increase3(z))