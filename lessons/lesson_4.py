import time
from datetime import datetime


def show_message(friend: str, c: str = '+') -> str:
    return f"""
____________{c}{c}{c}{c}{c}{c}{c}__{c}{c}__{c}{c}{c}{c}{c}{c}{c}
__________{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}__{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}{c}
_________{c}{c}{c}{c}______{c}{c}{c}{c}{c}{c}______{c}{c}{c}{c}
_________{c}{c}{c}{c}________{c}{c}________{c}{c}{c}{c}
__________{c}{c}{c}____{c}{c}{friend}{c}{c}____{c}{c}{c}
___________{c}{c}{c}{c}____{c}{c}{c}{c}{c}{c}____{c}{c}{c}{c}
_____________{c}{c}{c}{c}____{c}{c}____{c}{c}{c}{c}
_______________{c}{c}{c}{c}______{c}{c}{c}{c}
_________________{c}{c}{c}{c}__{c}{c}{c}{c}
___________________{c}{c}{c}{c}{c}{c}
_____________________{c}{c}
"""
def show_time() -> str:
    return str(datetime.now())

friends=['Dasha', 'Zlata', 'Nikita']
for friend in friends:
    print(show_message(friend=friend, c='5'))


print(show_time())

def get_sum(x:int, y:int)-> int:
    return x+y

print(get_sum(x=3, y=7))

def show_sum(x:int, y:int)-> None:
    print(x+y)

show_sum(x=3, y=7)