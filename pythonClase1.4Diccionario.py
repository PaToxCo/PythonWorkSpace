#Asi definimos el diccionario
miPrimerDiccionario = {}
datosPersonales = {"nombre": "jimena","edad": "50", "signo": "picis"}
print(datosPersonales)

#lit corrobora que es un diccionario
print(type(miPrimerDiccionario))

#accedemos por el valor no por la lista
print(f"el nombre de la persona ganadora es {datosPersonales["nombre"]}")
print(f"el signo de la persona ganadora es {datosPersonales.get("signo")}")