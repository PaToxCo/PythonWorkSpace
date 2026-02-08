propertys = ["jimena ezquiso","jimena amable", "jimena loca"]
stade = ["curable","incurable","en proceso"]

propertysMain = {
    "propiedades": [
        {
            "id": "1",
            "nombre": "jimena",
            "estado": True,
            "signo": "sagitario",
            "direccion": ("su casa", ),
            "cualidades": ["amable","feliz","graciosa","paranoica"]
        },
        {
            "id": "2",
            "nombre": "rodrgo",
            "estado": True,
            "signo": "geminis",
            "direccion": ("su casa",),
            "cualidades": ["amable","feliz","gracioso"]
        }, 
        {
            "id": "3",
            "nombre": "copito",
            "estado": True,
            "signo": "geminis",
            "direccion": ("su casa",),
            "cualidades": ["dormilon","ruidoso","gracioso"]
        }, 
    ]
}

msg = """
    -----Bienvenido al mundo magio de jimena-----
    1. Mostrar propiedades
    2. Ver canditadd de propiedades
    3. Ver primera y ultima
    4. Agregar caracteristica
    5. Salir
"""
print(msg)

opcion=int(input("Ingrese su opcion: "))

if opcion == 1:
    print(propertysMain["propiedades"])
elif opcion == 2:
    print(len(propertysMain))
        #pass da relleno para auqnue no haga nada igual recorra lo que sigue, 
        #break rompe la busqueda se encuentra o se hace lo q quieras y se rompe
        #continue rompe esta vuelta y lo hace en la siegueinte 

elif opcion == 3:
    print(propertys[0],stade[0],propertys[-1],stade[0])

elif opcion == 4:
    #new_property=input("ingrese la nueva caracteristica: ")
    #propertys.append(new_property)
    
    #hacemos que los id se generen solos
    idValue = len(propertysMain["propiedades"]) + 1

    #Creamos un nuevo diccionario para agregar a la lista Principal
    newProperty={}
    newProperty["id"]=idValue #el id se guarda 

    #pedimos el nombre
    nombreNew=input("Ingrese el nombre: ")
    newProperty["nmombre"]=nombreNew

    #pedimos el signo directamente
    newProperty["signo"]=input("ingrese el signo: ")

    newProperty["estado"] = True
    newProperty["cualidades"] = []

    #asi se grega info en un tupla
    infodireccion = input("Ingrese direccion")
    newProperty["direccion"] = (infodireccion,)

    #y lo agregamos al main
    propertysMain["propiedades"].append(newProperty)
    print(propertysMain["propiedades"])
else:
    print("ingrese una opcio valida")