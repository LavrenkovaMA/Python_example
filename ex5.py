# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

print("введите a")
a = int(input())

if (a%5 ==0) and not(a%30 ==0): 
    print ("кратно 5")
if (a%10 ==0) and not(a%30 ==0): 
    print ("кратно 10")
if (a%15 ==0) and not(a%30 ==0): 
    print ("кратно 15")
else:
     print("не кратно 5,10 и 15, но возможно кратно 30")
