
cant_dias = 15000
total = 0

while True:
    print("""
    1. Datos 
    2. Buscar
    3. Retirarse
    4. Salir""")


    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion in (1,2,3,4):
                break
            else:
                print("ERROR! DEBE INGRESAR UN NÚMERO DE 1 A 4!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")

    if opcion == 1:
        while True:
            try:
                rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
                if rut >= 1000000 and rut <= 99999999:
                    break
                else:
                    print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
            except:
                print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            

        while True:
            nombre = input("Ingrese nombre del dueño: ")
            if len(nombre.strip()) >= 3 and nombre.isalpha():
                break
            else:
                print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")
            
        while True:
            nombre_m = input("Ingrese nombre de la mascota: ")
            if len(nombre_m.strip()) >= 3 and nombre_m.isalpha():
                break
            else:
                print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")
            
        while True:
            try:
                dias =int(input("Ingrese cantidad de dias que se quedara: "))
                if dias >= 1 and dias <= 10:
                    break
                else:
                    print("ERROR! DEBE INGRESAR DE 1 A 10 DIAS")
            except:
                print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")
          
    elif opcion == 2:
        while True:
            try:
                rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
                if rut >= 1000000 and rut <= 99999999:
                    break
                else:
                    print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
            except:
                print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")  

    elif opcion == 3:
        while True:
            print("SU TOTAL A PAGAR ES",cant_dias)
            if dias == dias * cant_dias:
                break
                cant_dias = total
                break
                











         