a=4
b=8

# str.format()
c="{} < {}".format(a,b)
print(c);

# f strings
d = f'a is {a} and b is {b}'
z = f"a is {a} and b is {b}"
y = f'''a is {a} and b is {b}'''
print(d)
print(z)
print(y)

e = "%d < %d --> A %s" %(a,b,"string")
print(e)