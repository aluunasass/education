class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    def check_age(self):
        if self.age >= 18:
            print(f"{self.name} взрослый ")
        else:
            print(f"{self.name} малявка")
number=5
friend='dasha'
friends=[friend,'zlata', 'nikita']
friends[2]='vika'
print(friends)
friends_age={
    'dasha':12,
    'nikita':25,
    'zlata':11
}
print(friends_age['nikita'])
for name, age in friends_age.items():
    person=Person(name, age)
    person.check_age()