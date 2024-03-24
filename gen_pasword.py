import random
k = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

jas = int(input("escribe la longitud de tu contraseña = "))

password = ""

for i in range(jas):
    password += random.choice(k)

print(password)
