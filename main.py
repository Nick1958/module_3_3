# Домашнее задание по уроку "Распаковка позиционных параметров" модуль 3_3

#  1. Функция с параметрами по умолчанию:

def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(3)
print_params(0,[5,7], False)
print_params('abc',True,{'a':5, 'c':7})
print_params(6, 7, [1, 2, 3])
print_params(b = 25), print_params(c = [1,2,3])
# print_params(6, 7, c) # Error
print()


# 2.Распаковка параметров:

values_list = [1,'abc', False]
values_dict = {'a': 2024, 'b': 24.0, 'c': 'октябрь'}
print_params(*values_list)
print_params(**values_dict)
print()


# 3.Распаковка + отдельные параметры

values_list_2 = [24.11,'элемент']
print_params(*values_list_2, 42)
