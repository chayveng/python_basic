print("Hello,Pyhon")

a = 10  # INTEGER
b = 10.5  # FLOAT
cc = "h"  # character
c = "hello"  # STRING, Object
d = [
    1,
    2,
    3
]  # LIST, Array, Ojbect
e = {"name": "John", "age": 30}  # Object
f = True  # BOOLEAN

print(d)
print(d[2])

sum = d[2] + d[0]

length = len(c)
print("length of c:", length)

ee = [
    {"name": "John", "age": 30},
    {"name": "Snow", "age": 15}
]

person = ee[0]
name = person["name"]
print(name)

name = ee[0]["name"]
age = ee[0]["age"]

print("name", name, "age", age)

title_name = "Name:"
title_age = "Age:"

print(title_name)
print(name)
print(title_age)
print(age)

print(title_name, name, title_age, age)

for index, var in ee.items():
    print(var)
