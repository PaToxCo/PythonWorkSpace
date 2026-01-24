msg="""
    Hola bienvenido a detector de locas

    1. Nombre
    2. DNI
    3. Apellido
    4. Signo
    5. Edad
"""

print(msg)
nombre = input("Ingrese su nombre: ")
dni = input("Ingrese su dni: ")
apellido = input("Ingrese su apellido: ")
signo = input("Ingrese su signo: ")
edad = int(input("Ingrese su edad: "))

estaLoca = nombre == "Jimena" and signo == "sagitario" and edad == 21
if(estaLoca == True):
    print(f"El test salio que la paciente {nombre} que esta bien loca") 
else:
    print("Esta totalmente cuerdo y sano")
