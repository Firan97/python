from functools import reduce
def mul_list(el_1, el_2):
    return el_1 * el_2

uniq_list = [el for el in range(100, 1001, 2)]
print(f"List {uniq_list} Multiplication of numbers {reduce(mul_list , uniq_list)}")