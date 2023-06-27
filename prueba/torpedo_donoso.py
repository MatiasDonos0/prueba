# torpedo GG 

def validar_opcion():
    while True:
        try:
            opcion = int(input("Escoga una opción del Menú 1 a 7 : "))
            if opcion in(1,2,3,4,5,6,7):
            else:
                print("ERROR! Escoga un numero del 1 a 7")
        except:
            print("ERROR! debe ser un número entero")

def validar_auto(m_augo):
    while True:
        try:
            autos = int(input("Ingrese cantidad de auto : "))
            if auto in(m_auto):
            else:
                print("ERROR! NÚMERO DE AUTO NO DISPONIBLES!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_edad():
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if edad >= 18 and edad <= 100:
                return edad
            else:
                print("ERROR! LA EDAD DEBE ESTAR ENTRE 18 Y 100")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_correo():
    while True:
        correo = input("Ingrese correo: ")
        if "@" in correo:
            return correo
        else:
            print("ERROR! CORREO INCORRECTO!")

def validar_cantidad_prod():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad >= 0:
                return cantidad
            else:
                print("ERROR! CANTIDAD DEBE SER 0 O POSITIVA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_marca_auto():
    while True:
        marca = input("¿Que marca elige comprar (Nissan, Chevrolet, Renault?")
        if marca.lower() == "renault" or marca.lower() == "volvo" or marca.
        lower()=="masda":
            print(f"disfrute su nuevo {marca}")
            return marca
        else:
            print("No tenemos disponible esa marca")

def validar_color_auto():
    while True:
        color= input("¿Que color  elige comprar (Blanco, Rojo, Gris, amarillo y rosado?")
        if color.lower() == "blanco" or color.lower() == "rojo" or color.lower()=="gris" or color.lower() == amarillo or color.lower()== rosado
            return color
        else:
            print("No tenemos disponible esa marca")
    



            
            

def validar_estatura():
    while True:
        try:
            estatura = float(input("Ingrese estatura(m): "))
            if estatura >= 0.1 and estatura <= 3:
                return estatura
            else:
                print("ERROR! LA ESTATURA DEBE ESTAR ENTRE 0.1 y 3 metros!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")

def validar_clave():
    while True:
        clave = input("Ingrese clave: ")
        validar_clave = input("Ingrese nuevamente la clave: ")
        if len(clave)>=6 and len(clave)<=16 and clave==validar_clave:
            break
        else:
            print("ERROR! largo incorrecto o claves no coinciden!")

def validar_telefono():
    while True:
        try:
            telefono = int(input("Ingrese teléfono: "))
            if len(str(telefono))==9:
                break
            else:
                print("ERROR! el teléfono debe tener 9 dígitos!")
        except:
            print("ERROR! debe ingresar ingresar un número entero!")

def validar_genero():
    while True:
            genero = input("Ingrese género(F,M,O): ")
            if genero.upper() in("F","M","O"):
                break
            else:
                print("ERROR! el género debe ser f, m, o!")
