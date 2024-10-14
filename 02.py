import os 
os.system ("cls")

multiplicando = int (input("multiplicando: ")) 
multiplicador = int (input("multiplicador: "))

producto = 0

while multiplicador > 0:
    producto += multiplicando
    multiplicador -= 1

print (f"producto: {producto}") 


def multiplica (n1,n2):
    if n2 == 1: return n1 
    return n1 + multiplica (n1,n2-1)
