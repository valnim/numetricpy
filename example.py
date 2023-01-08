from numetric import UnitValue

x = UnitValue(10, 'm*s^2')
y = UnitValue(5, 'm*s^-1')
z = UnitValue(2, 'm*s^2')

a = x + z
b = x - z
c = x * y
d = x / y
e = x ** 2

print(x > z)
print(x >= z)
print(x < z)
print(x <= z)
print(x == x)

xstr = repr(x)

print(a)
print(b)
print(c)
print(d)
print(e)

input("Press any key to continue...")




