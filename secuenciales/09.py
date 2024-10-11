num = int(input("ingresa un número entero de 4 cifras: "))

if 1000 <= num <= 9999:
    suma = 0
    for cifra in str(num):
        suma += int(cifra)
    print("La suma de las cifras es:", suma)
else:
    print("ingresar un número de 4 cifras.")

