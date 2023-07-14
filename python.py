# Задание

# Написать функцию, которая создает список длиной 10 и заполняет его случайными числами от 0 до 3. Показать список в консоль.
# Написать функцию, которая выводит в консоль количество каждого числа в списке.

# Пример:
# [1, 2, 1, 2, 0, 3, 2, 2, 1, 1]
# 0 - 1
# 1 - 4
# 2 - 4
# 3 - 1

# То есть в примере выше нулей одна штука, единиц 4 штуки, и т.д

import random

inputListLength = int(input("List leght -"))
userRangeOfNum = int(input("Renge from 0 - "))


def createListWithNumbers(listLength, rangeOfNum):
    x = 0
    listWithNumbers = []
    while x < listLength:
        listWithNumbers.append(random.randint(0, rangeOfNum))
        x += 1
    return listWithNumbers


print(createListWithNumbers(inputListLength, userRangeOfNum))
