a = 5
print(a)

b = 25.7
print(type(b))

a_b = a + b
print(a_b)

c = "Sasha"
print(type(c))

d = ["Lena", "Vasya"]
print(d)

d.append(c)
print(d)
print(d[1])

# name = input('Введите свое имя:')
# print(f'Ваше имя: {name}')

print(type(a))
print(type(b))
print(type(a_b))
print(type(c))
print(type(d))

family = {
    "Sasha": 11,
    "Nikita": 25,
    "Lesha": 17,
}
print(family)
print(type(family))
print(family["Lesha"])
family["Lesha"] = 18
print(family)

print(family["Sasha"] == family["Lesha"])
print(family["Sasha"] > family["Lesha"])
print(family["Sasha"] < family["Lesha"])
print(type(family["Sasha"] < family["Lesha"]))

f = None
print(bool(f))

animals = ["dog", "cat", "hamster"]
print(animals)
