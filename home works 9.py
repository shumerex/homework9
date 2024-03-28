def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызов функции c указанием всех трех параметров
print_params(10, 'новая строка', False)


# Вызов функции с указанием только одного параметра
print_params(5)


# Вызов функции без аргументов (используются значения по умолчанию)
print_params()

# Вызов функции с передачей значения только для параметра b
print_params(b=25)


# Вызов функции с передачей списка в качестве значения параметра c
print_params(c = [1, 2, 3])



# Создаем список с тремя элементами разных типов
values_list = [42, 'hello', 3.14]

# Создаем словарь с тремя ключами и значениями разных типов
values_dict = {'a': True, 'b': [1, 2, 3], 'c': {'key': 'value'}}

# Определяем функцию print_params для распаковки параметров
def print_params1(a, b, c):
    print(a, b, c)

# Передаем values_list и values_dict в функцию print_params с распаковкой параметров
print_params1(*values_list)
print_params1(**values_dict)

# Создание списка
values_list_2 = [10, 'world']

# Проверка вызова с дополнительным параметром
print_params(*values_list_2, 42)