import os
os.system ("cls")

num = int (input("ingrese un numero: "))
factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print (f"factorial: {factorial}")