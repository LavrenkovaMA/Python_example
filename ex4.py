# #Показать первую цифру дробной части числа
# num = 1.396
# for c in str(num):
#     if c == ".":
#         check = True
#     if check:
#         print(c)
#         break
    
# a=1.745
# print(int(((a*10) % 10)))
a = 1.8665
c = round(a,2)
print(str(c)[-2])