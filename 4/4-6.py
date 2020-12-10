from itertools import count, cycle
print("Генератор числа с указанного .Для выхода q")
for i in count(int(input('Стартовое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

        print("Программа повторяет элементы списка. Для выхода q")
        u_list = input('Введите список , разделяя пробелом:').split()
        iter = cycle(u_list)
        quit = None
        while quit != 'q':
            print(next(iter), end='')
            quit = input()