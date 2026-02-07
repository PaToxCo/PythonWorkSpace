ListaCopito=[1,2,3,'dos',5]
print(ListaCopito[0])
print(ListaCopito[1])

#Muestra el ultimo de la lista
print(ListaCopito[-1])

#Muestra el tipo o sea lista
print(type(ListaCopito))

#Asignamos un valor en la posicon 1
ListaCopito[1]=10
print(ListaCopito)

#Concatenamos listas
ListaTotal=ListaCopito+ListaCopito
print(ListaTotal)

#Apprend agrega valores a la lista
ListaCopito.append('tres')
print(ListaCopito)

#Mostramos un espacio especifico de la lista
print(ListaCopito[1])

valor = input("Ingresa un numero: ")
ListaCopito.append(valor)
print(ListaCopito)
print(f"la lista ahora tiene el numero {ListaCopito[-1]} como nuevo valor")

#Remove remueve el valor de la lista, si son muchos remueve el primero que encuentre
valor = input("ingresa el valor que quieras remover: ")
ListaCopito.remove(valor)
print(f"La nueva lista es {ListaCopito}")

#Cuanta cuantas veces aparece el valor puesto
print(ListaCopito.count(10))

#Reverse voltea la lista
ListaCopito.reverse()
print(ListaCopito)

#inder te da la posicion que tiene el valor en la lista
print(ListaCopito.index(10))

#sort ordena la lista
ListaNumeros=[1,3,4,6,5,1,3,6,5]
ListaNumeros.sort()
print(ListaNumeros)

# in ayuda a saber si algo esta en una lista
4 in ListaNumeros

if 4 in ListaNumeros:
    print("el numero 4 si esta en la lista")

# not in para saber si no esta
9 not in ListaNumeros

#tambien funciona en strings
print('b' in 'burro')
msg = 'burro'
print(msg[1])


#Esta es una super lista osea una matriz
lista1 = ["hola","Chau","cacahuate"]
lista2 = [1,2,3,4]
lista3 = ['222','3333']
ListaTodo=[lista1,lista2,lista3]
print(ListaTodo)
#aca podemos ver que toma la lista en el indice 0 que es la lista1 y dentro de ella el indice 0 que es hola
print(ListaTodo[0][0])