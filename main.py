from ValuesWithUnits import ValueWithUnit

x = ValueWithUnit(10, 'm*s^2')
y = ValueWithUnit(5, 'm*s^-1')
z = ValueWithUnit(2, 'm*s^2')

a = x + z
b = x - z
c = x * y
d = x / y
e = x ** 2


print(a)
print(b)
print(c)
print(d)
print(e)

input("Press any key to continue...")




