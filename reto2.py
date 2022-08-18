# Multiplo de 3
numero = int(input("Digita un numero entero: "))
modulo = numero % 5
print(f'El modulo del numero es: {modulo}')

#CONDICIOONES

#if()
if modulo == 0 :
    print(f'El numero {numero} es multiplo de 5')
else:
    print(f'El numero {numero} no es multiplo de 5')
print("finalizar el programa")
