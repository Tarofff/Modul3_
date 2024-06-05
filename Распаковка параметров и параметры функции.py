def print_params(a = 1, b = 'строка', c = True):#Создайте функцию
    print(a, b, c)
values_list = [1, 'строка', True]#Создайте список values_list с тремя элементами разных типов
dict_values_list = {'a':1, 'b':'строка', 'c':True}#Создайте словарь с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов
values_list_2 = [1,'строка']#cоздайте список values_list_2 с двумя элементами разных типов
print_params(1,'строка',  True)#выводить эти параметры
print_params(2)#Вызовите функцию print_params с разным количеством аргументов
print_params()#вызов без аргументов
print_params(b = 25)#Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(c = [1,2,3])
print_params(*values_list)#Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря)
print_params(**dict_values_list)
print_params(*values_list_2,42)