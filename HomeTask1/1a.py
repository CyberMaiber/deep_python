#Написать программу, которая будет выводить в консоль ёлочку заданной высоты

height = int(input("Введите высоту ёлочки: "))

for i in range(1, height+1):
    print(" "*(height-i) + "*"*(2*i-1))