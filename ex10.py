#Найти расстояние между двумя точками пространства
import math
a = [1, 2, 7]
b = [3, 5, 10]

s = math.sqrt(((b[0]-a[0])**2)+((b[1]-a[1])**2)+((b[2]-a[2])**2))
print(round(s))

# math.sqrt - квадратный корень из числа