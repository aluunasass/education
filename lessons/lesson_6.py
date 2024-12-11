# from lessons.lesson_2 import family
from lessons.lesson_5 import game
if __name__ == '__main__':
    try:
        game()
        # number = 1 / 3
        # print(family['Dasha'])
    except ValueError:
        print('Вы ввели не цифру')
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
    except Exception as e:
        print(f'Ошибки {e}')
    else:
        print('Программа успешно закончена')
    finally:
        print('Программа завершена')
