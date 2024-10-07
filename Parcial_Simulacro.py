# # Gestión de Inventario
# # La Empresa “Empire Inventory” necesita desarrollar un sistema de administración de
# # productos para sus almacenes. Para cada producto se almacenará:
# # • Nombre del producto.
# # • Precio del producto.
# # • Cantidad del producto.
# # La información de los productos se almacenará en un arreglo bidimensional, donde cada fila
# # # representara un producto y las columnas contendrán los datos mencionados.

inventario = []
def menu_principal():
    opcion = 0
    while opcion != 4:
        print("\n-----Menu principal-----")
        print("1.---Carga")
        print("2.---Buscar Producto")
        print("3.---Ordenar inventario")
        print("4.---Mostrar producto mas caro ")
        print("5.---Mostrar productos mas barato")
        print("6.---Mostrar Productos con precio a 15000")
        print("7. Salir del sistema")
        opcion = int(input("Seleccione una opcion del 1 al 5: "))
        match opcion:
            case 1:
                cargar_inventario()
            case 2:
               buscar_producto()
            case 3:
                Ordenar_inventario()
            case 4:
                producto_caro()
            case 5:
                producto_barato()
            case 6:
                producto_15000()
            case 7:
                print('Saliendo del menu...')
                break
            case _:
                print('Opcion erronea, seleccione un numero del 1 al 5 porfavor.')
# 2. Cargar inventario:
# • Desarrollar una función que permita al usuario ingresar los datos del o los
# productos en una matriz (nombre, precio, cantidad).
# • El sistema debe permitir al usuario ingresar la cantidad deseada de productos.
def cargar_inventario():
    nombre = input('Ingrese el nombre del producto: ')
    precio = int(input('Ingrese el precio del producto: '))
    cantidad = int(input('Ingrese la cantidad del producto: '))
    producto_nuevo = [nombre, precio, cantidad]
    inventario.append(producto_nuevo)
    print(f"El producto: '{nombre}' fue agregado al inventario.")
# 3. Buscar producto:
# • Implementar un algoritmo de búsqueda que permita al usuario encontrar un
# producto específico por su nombre y muestre por pantalla todos los datos de
# ese producto (nombre, precio y cantidad). 
def buscar_producto():
    buscar_por_nombre = input('Ingrese el nombre del producto a buscar: ')
    find = False
    for producto in inventario:
        if producto[0].lower() == buscar_por_nombre.lower():
            print(f'El producto encontrado fue:{producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")')
            find = True
            break
        if not find:
            print ('Producto no encontrado')
        
        
# 4. Ordenar inventario:
# • Utilizar un algoritmo de ordenamiento para ordenar los productos en función
# de su precio de manera ascendente y luego mostrar por pantalla los productos
# ordenados.
def Ordenar_inventario(): 
    if len(inventario) <= 1:
        return inventario
    
    pivote = inventario[-1]
    order_left = []
    order_right = []
    
    for producto in inventario[:-1]:
        if producto[1] <= pivote[1]:
            order_left.append(producto)
        else:
            order_right.append(producto)
        return Ordenar_inventario(order_left) + [pivote] + Ordenar_inventario(order_right)
inventario_ordenado = Ordenar_inventario()
print('Inventario ordenado por precio:', inventario_ordenado)
# 5. Mostrar producto más caro:
# • Desarrollar una función que identifique y muestre el producto más caro del
# inventario.
def producto_caro():
    if producto not in inventario:
        print('El producto no se encuentra en el inventario')
        return
    for producto in inventario:
        if producto[1] > producto_caro[1]:
            producto_caro = producto
def producto_15000():
    productos_mayores_15 = []            
    for producto in inventario:    
        if producto[1] > 15000:
            productos_mayores_15.append(producto)
            print(f"Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")
        else:
            print("No hay productos con precio mayor a 15000.")
            
# 6. Mostrar producto más barato:
# • Desarrollar una función que identifique y muestre el producto más barato del
# inventario.
def producto_barato():
    if producto not in inventario:
        print('El producto no se encuentra en el inventario')
        return
    for producto in inventario:
        if producto[1] < producto_barato[1]:
            producto_barato = producto
            print(f"Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}")

menu_principal()


# Requerimientos:
# El sistema deberá constar de los siguientes puntos:
# 1. Menú Principal: Mostrar un menú con las siguientes opciones disponibles:
# • Cargar producto/s.
# • Buscar producto.
# • Ordenar inventario.
# • Mostrar producto más caro y más barato.
# • Mostrar productos con precio mayor a 15000.
# • Salir
# Requisitos técnicos:
# ▪ Utilizar funciones para cada una de las operaciones mencionadas.
# ▪ Mantener una estructura de código limpia y bien comentada.
# ▪ Si el usuario selecciona cualquier opción sin que existan productos registrados en el
# sistema, aparecerá un mensaje en pantalla notificando que no hay productos
# disponibles para la operación solicitada.
# Entrega del programa
# ▪ La entrega se deberá realizar mediante el link al repositorio de GitHub