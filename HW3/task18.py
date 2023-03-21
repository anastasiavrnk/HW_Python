# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X   

n = int(input())
list_1 = list()
for i in range(n):
    a = int(input())
    list_1.append(a)
print(list_1)
x = int(input())
list_2 = list()
for j in range(len(list_1)):
    list_2.append(x - list_1[j])
print(list_2)
print(list_1[list_2.index(min(list_2))])