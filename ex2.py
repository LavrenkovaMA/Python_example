#Найти максимальное из пяти чисел

number_list = []
for i in range(5):
    number_list.append(int(input(f"Введтите {i+1} число  ")))
print(f"Максимальное число из введенных: {max(number_list)}")
