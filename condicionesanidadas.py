#condiciones anidadas elif

sensorNivelAgua=(input("Digite el nivel de agua actual"))

if(sensorNivelAgua>=0 and sensorNivelAgua<20):
    print(f'Peligro el nivel {sensorNivelAgua} es peligroso')
elif(sensorNivelAgua>=20 and sensorNivelAgua<400):
    print(f'Hidroituango funcionando ok {sensorNivelAgua}')
elif(sensorNivelAgua>=400):
    print(f'Peligro el nivel {sensorNivelAgua} es peligroso')
else:
    print("El nivel de agua no es valido")