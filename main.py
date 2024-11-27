   # !5 = 1*2*3*4*5 = 120
   # сравнение числа с 0 , если 0 то возврат 1
   # создание переменной для хранения итогового результата
   # с помощью цикла for и range перебираем числа до нашего числа включительно, у которого мы вычисляем факториал
   # результирующую переменную умножаем на текущее число в цикле
   # возвращаем факториал

def factorial(number):
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

# result = 1
# result = 1*1 = 1
# result = 1*2 = 2
# result = 2*3 = 6
# result = 6*4 = 24
# result = 24*5 = 120
# return = 120*6 = 720
# return = 720*7 = 5040

print(factorial(7))