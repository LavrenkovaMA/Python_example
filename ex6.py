# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

list =["","MONDAY", "TUESDAY", "WEDNESDAY","THURSDAY","FRIDAY", "SATURDAY", "SUNDAY"]
print("введите число от 1 до 7")
i= int(input())

if i == 6 or i ==7:
    print(list[i], "выходной день")
else:
    print(list[i], "будний день")