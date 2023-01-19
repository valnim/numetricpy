from numetricpy.numetricpy import UnitValue

# Example file for use of numetricpy

x = UnitValue(10, 'm*s^2')
y = UnitValue(5, 'm*s^-1')
z = UnitValue(2, 'm*s^2')
bar = UnitValue(1, 'bar')

a = x + z
b = x - z
c = x * y
d = x / y
e = x ** 2
f = x * 2
g = 2 * x
h = x / 2
i = 2 / x
j = i * x


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
print(f)
print(bar)
print(bar.str_as('bar'))
print(bar.str_as('Pa'))

input("Press any key to continue...")




