# Создайте функцию three_args(), которая принимает 1, 2 или
# 3 строго ключевых параметра. В результате ее работы на
# печать в консоль выводятся значения переданных
# переменных, но только если они не равны None. Получим,
# например, следующее сообщение: «Переданы аргументы:
# var1 = 2, var3 = 10»

def three_args(**kwargs):
    return kwargs


print(f"Переданы аргументы: {(three_args(var1=2, var3=10, var2=3, var4=70))}")
