# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 18:48:45 2021

@author: ИнтелАв
"""

#Задание 1. Вызвается командой CMD "python homework_test.py 10 1 2"

from sys import argv

name, vyranotka, vremya_raboty, premiya = argv

print("Зарплата составляет: ", int(vyranotka) * int(vremya_raboty) + int(premiya))

#задание 2

num = [1, 2300, 6565, 565, 1 , 3 , 10, 20, 70, 10, 30]
list2 = [num[i] for i in range(0, len(num)) if i > 0 and num[i] > num[i-1]]

#Задание 3

home3 = [x for x in range(20,241) if x % 20 == 0 or x % 21 == 0] 

#Задание 4

num4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
num4_end = [x for x in num4 if num4.count(x) == 1]

#Задание 5

from functools import reduce
def my_func5(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el

num5 = [x for x in range(100,1001) if x % 2 == 0]
print(reduce(my_func5, num5))

#Задание 6 

from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)
        
        
#через 5 секунд выходим        
from itertools import cycle
import time
start = time.time() 
for el in cycle("Привет"):
    if  time.time() - start  > 5:
        break
    else:
        print(el)

#Задание 7
def fact(n):
    rez = 1
    for el in range(1,n+1):
        rez = rez * el
        yield rez
        
n = 6
for el in fact(n):
    print(el)

