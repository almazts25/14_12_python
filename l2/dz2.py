x = int(input('Type a number: '))
a, b = divmod(x, 1000)
c, d = divmod(b, 100)
e, f = divmod(d, 10)
print(a)
print(c)
print(e)
print(f)


