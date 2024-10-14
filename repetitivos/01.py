import os
os.system ("cls")

dividiendo = int (input("dividendo: "))
divisor = int (input("divisor: "))

cociente = 0
while dividiendo >= divisor:
    cociente += 1
    dividiendo -= divisor

    print (f"cociente: {cociente}")
    print (f"residuo: {dividiendo}")
