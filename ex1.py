# По двум заданным числам проверить является ли одно квадратом второго 
# number1= 2
# number2= 8
# if number1*number1 == number2:
#     print("b является квадратом a")
# else :
#     print("b не является квадратом a")

print("введите a")
a = int(input())
print("введите b")
b = int(input())

if a**2 == b:
    print("b является квадратом a")
elif b**2 == a:
    print("a является квадратом b")
else:
    print("ни одно число неявляется квадратом второго")