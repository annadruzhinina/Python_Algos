"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
def reverse(number):
    """---"""
    result = ""
    while number > 0:
        one_number = number % 10
        result = result + str(one_number)
        number = number // 10
    print(result)

# start
X = int(input(f"Введите число: "))
reverse(X)
