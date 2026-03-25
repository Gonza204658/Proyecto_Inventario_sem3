def agrega_producto (inventario, nombre, precio, cantidad): #aqui recibe los datos que le enviaron en el otro archivo que es app.py y 
    produc_guardados = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(produc_guardados)  # aqui lo que haces es oye lo que hay en la variable proc_guardados, añadelos al inventario
    # Aqui en resumidas cuentas se recibe el inventario y ademas de eso, los datos que el usuario manda, en la variable prodc_guardados
    # va guardar los datos que se ingrese y como tenemos el inventario, este lo guarda.

def mostrar_inventario(inventario): #AQui recibimos el inventario que se tiene
       if len(inventario) == 0: # aqui len hace un recorido, el cuenta lo que hay en inventario, y le decimos, si en el recorrido que hagas sea igual a 0, o sea q no haya nada
                                #manda un mensaje de "inventario vacio"
        print("El inventario está vacío")
       else:                               # de lo contrario si no se cumple la primera condicion, o sea que si haya algo
           for mostrar_prod in inventario:  #usaremos for para hacer un recorrido de todo lo que haya en inventario
              print(mostrar_prod)            # y inprimimos la variable que creamos y es la que tiene lo que hay en el inventario

def buscar_producto(inventario , nombre_prod_buscar): #aqui recibimos los datos que me envia el usuario, osea, en nombre_prod_buscar esta lo que me envia el usuario
    for productos_inven in inventario: #usamos for para que recorra el inventario y lo metemos en productos_inven
        if productos_inven["nombre"] == nombre_prod_buscar: # aqui le decimos si en la columna nombre es igual a los que el usuario ingreso
            return productos_inven #devuelve lo que encontro, o sea el producto
    return None # si no, no se encontro nada

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None): 
    # Esta función sirve para buscar un producto dentro del inventario
    # y actualizar su precio y/o cantidad.
    #
    # en los parametros recibe el inventario que le enviamos
    # nombre del producto que queremos actualizar
    # nuevo precio (opcional, puede venir o no)
    # nueva_cantidad (opcional)
    # None significa "no me dieron ese valor"
    # es decir, no quiero cambiar ese dato, es decir, si no le escribieron nada en esa caja de precio, el deja el que estaba

    producto_cambiar = buscar_producto(inventario, nombre)
# aqui llamamos la funcion buscar productos y le pasamos el inventario y el nombre
    #
    # Puede pasar 2 cosas:
    # 1. Si encuentra el producto, devuelve el diccionario del producto
    # 2. Si no lo encuentra, devuelve None
    # Ese resultado lo guardamos en la variable producto_cambiar

    if producto_cambiar: #esta parte lo que hago es validar si encontro el producto que estabamos buscando
        # y si es así, haz lo siguiente
        if nuevo_precio is not None: #aqui preguntamos si el usuario dio un nuevo precio
            # Usamos 'is not None' porque None significa que no nos dieron ese dato
            # Si el usuario sí escribió un precio entra aquí 
            producto_cambiar["precio"] = nuevo_precio # aqui cambiamos el diccionario, en la seccion de precio y 
            #decimos que ahora va ser igual a nuevo_precio, osea el que le enviamos 

        if nueva_cantidad is not None:                     #aqui es practicamente lo mismo
            producto_cambiar["cantidad"] = nueva_cantidad

        return True
        #esto me dice se encontró el producto y se actualizó        
        # Este valor se devuelve al app.py para que el programa sepa que todo salió bien 

    else: #Este else se ejecuta si el producto no se encontro es decir, si producto_cambiar era None
        return False #esto devuelve que no se encontro

def eliminar_producto (inventario, producto_eliminar): # aqui recibimos los datos que nos envian en los parametros

    busca_producto_eliminar = buscar_producto(inventario, producto_eliminar) # le creamos una variable donde va tener la funcion
    #buscar_producto, este recibe el inventario y el producto a eliminar que se le pidio, y te lo buscará

    if busca_producto_eliminar: #si encuentra el producto 
        inventario.remove(busca_producto_eliminar) #aqui vamos a tomar el inventario y le decimos que remueva el producto que le pedimos  
        return True # devulve verdadero si se encuentra y lo envia a app.py
    else:
        return False #devolvemos falso si no se encuentra y lo mismo, se envia a app.py
    
def calcular_estadisticas(inventario): #recibimos el inventario 
    unidades_totales = 0   #creamos variables que vamos a usar mas adelante, 
                            #validamos en 0 para ingresarles valores
    valor_total = 0
    producto_mas_caro = None    # Aquí guardaremos el producto con mayor precio
                                # Empieza en None porque todavía no sabemos cuál es   
    producto_mayor_stock = None

    for producto in inventario:
        # Recorremos uno por uno todos los productos del inventario
        #  "producto" es cada diccionario dentro de la lista
        
        unidades_totales += producto["cantidad"] # suma la cantidad de productos y lo guardamos en unidades totales

        # calcular valor total
        subtotal = producto["precio"] * producto["cantidad"] # Calculamos cuánto vale ese producto en total y los guardamos en subtotal 
        valor_total += subtotal  # Sumamos ese subtotal al valor total del inventario

        # producto más caro
        if producto_mas_caro is None or producto["precio"] > producto_mas_caro["precio"]:

            # Aquí preguntamos
            # 1.Todavía no hay producto guardado? (None)
            # 2.Este producto es más caro que el anterior?

            producto_mas_caro = producto
            # Si se cumple alguna condición, guardamos este producto
            # como el más caro hasta ahora

        # producto con mayor stock
        if producto_mayor_stock is None or producto["cantidad"] > producto_mayor_stock["cantidad"]:
             # Preguntamos:
            # 1. ¿Aún no hay producto guardado?
            # 2. ¿Este tiene más cantidad que el anterior?
            producto_mayor_stock = producto
            #guardamos el que tiene mas valor

    return unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock #devolvemos todo lo que hemos hecho 