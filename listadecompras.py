lista_compras = [] #Es una lista

mas_productos = True #variable con booleano por la letra mayúscula

while mas_productos:
    compra_producto = input("¿Cuál es el siguiente producto que deseas agregar a la lista? ")
    lista_compras.append(compra_producto) #append permite agregar nuevos elementos a una lista

    seguir_agregando_productos = (input("¿Deseas seguir agregando más productos? (sí o no) "))

    if seguir_agregando_productos != "sí":
        mas_productos = False

print ("Los productos en la lista son: ")

for producto in lista_compras:
    print(producto)

productos_finales = lista_compras

import pywhatkit
pywhatkit.sendwhatmsg("+número de teléfono", "No olvides comprar %s" % productos_finales, 22, 52)