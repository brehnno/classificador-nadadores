Idade = int(input("Idade: "))

if Idade in range (5,7):
    print("Categoria Infantil A")

elif Idade in range (8,10):
    print("Categoria Infantil B")

elif Idade in range (11,13):
    print("Categoria Juvenil A")

elif Idade in range (14,17):
    print("Categoria Juvenil B")

else:
    print("Categoria Adulto")