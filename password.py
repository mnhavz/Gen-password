import random

minus="qwertyuiopasdfghjklzxcvbnm"
mayus=minus.upper()
numeros="1234567890"
simbol="@#€&$&+*<>"
base=minus+mayus+numeros+simbol
long=12

muestra=random.sample(base,long)

password="".join(muestra)
print(password)