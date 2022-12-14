"""
5. (МОДУЛЬ 2) создать модуль 2seq.py. Задание:
Пользователь вводит любые цифры через запятую
Сохранить цифры в список
Получить новый список в котором будут только уникальные элементы исходного (уникальным считается символ, который встречается в исходном списке только 1 раз)
Вывести новый список на экран
Порядок цифр в новом списке не важен
Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
Результат: 2, 4, 6, 9

(Дополнительно*) Предусмотреть что пользователь может использовать один из 3-х разделителей: запятую, точку с запятой,
слэш (1,2,3 1;2;3 1/2/3), но только какой то один 1,2;3/4 - так нельзя
"""

# Пользователь вводит любые цифры через запятую
user_numbers_list = input('Введите любые цифры через запятую:\n')
# замена разделителей, если пользователь ввел не через запятую. Создание списка
user_numbers_list = user_numbers_list.replace('/', ',').replace(';',',').replace('.', ',')
user_numbers_list = user_numbers_list.split(',')
# создание списка только с уникальными элементами
unique_numbers_list = list(set(user_numbers_list))

# вывод списка

print(*unique_numbers_list, sep = ', ')