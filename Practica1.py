productos = [] 

msg = """
    SISTEMA DE MERCADO - DATUX
    1. Sumar 2 numeros
    2. Crear coleccion de productos
    3. Agrega un nuevo producto
    4. Mostrar el producto de precio mas bajo
    5. Salir
"""

def sumar():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print("La suma es:", n1 + n2)

def crear():
    print("Coleccion creada!")

def agregar():
    nom = input("Nombre producto: ")
    pre = int(input("Precio: "))
    productos.append( {'nombre': nom, 'precio': pre} )

def masBarato():
    if len(productos) == 0:
        print("La lista esta vacia")
        return
    
    ganador = productos[0] 
    for p in productos:
        if p['precio'] < ganador['precio']:
            ganador = p 
    print("El mas barato es:", ganador['nombre'], "con precio", ganador['precio'])

while True:
    print(msg)
    opcion = int(input("Elige opcion: "))

    if opcion == 1:
        sumar()
    elif opcion == 2:
        crear()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        masBarato()
    elif opcion == 5:
        break 
    else: 
        print("Elige una opción valida")
