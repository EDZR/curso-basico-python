calificacion = input("Ingresa tu calificaion de AZ-900: ")
calificacion = int(calificacion)
if calificacion < 700: 
    print("Vees, por no estudiar")
elif calificacion > 1000 :
    print("Mientes, no puedes sacar mas de 1000")
else : 
    print("Felicidades pasa por tu certificado")

edad = input("Ingresa tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Eres mayor de edad")
elif edad > 100 : 
    print("Si vienes acompañad@ de tus abuelitos, si te podemos fiar")
elif edad <0 :
    print("Ni que fueras viajero del tiempo")
else : 
    print("Eres menor de edad")




    

