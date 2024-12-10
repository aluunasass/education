a = 5
print(a)

b = 25.7
print(b)

a_b = a+b
print(a_b)

c = 'Sasha'
print(c)

d = ['Lena', 'Vasya']
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

e = {
    'Sasha': 11,
    'Nikita': 25,
    'Lesha': 17,
}
print(e)
print(type(e))
print(e['Lesha'])
e['Lesha'] = 18
print(e)

print(e['Sasha'] == e['Lesha'])
print(e['Sasha'] > e['Lesha'])
print(e['Sasha'] < e['Lesha'])
print(type(e['Sasha'] < e['Lesha']))

f = None
print(bool(f))

animals=['dog','cat','hamster']
print(animals)
