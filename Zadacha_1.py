'''
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
'''
import math
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите степень числа: '))


def self_pow(number_1, number_2):
    if number_2 == 0:
        return 1
    return number_1 * self_pow(number_1, number_2-1)

print(self_pow(number_1, number_2))