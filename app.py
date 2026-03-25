import servicios #importamos el archivo servios donde estan todas mis funciones, y mas adelante llamaré a cada una de ella en base a cuando las necesite
import archivos

inventario = [] #Creamos una lista para almacenar todos los productos que ingrese el usuario

activador = True # creamos un activador, esto me ayuda a controlar el ciclo, cuando este sea verdadero
                 # se cerrará

while activador:
    print("\nHOLA USUARIO")  #creamos las opciones a escoger

    print(
        "\n1. AGREGAR PRODUCTOS" 
        "\n2. MOSTRAR INVENTARIO"
        "\n3. BUSCAR PRODUCTO"
        "\n4. ACTUALIZAR PRODUCTOS"
        "\n5. ELIMINAR PRODUCTOS"
        "\n6. CALCULAR ESTADISTICAS"
        "\n7. GUARDAR INVENTARIO EN CSV"
        "\n8. CARGAR INVENTARIO CSV"
        "\n9. SALIR"
    )

    escoger_op = input("¿QUE DEASEAS HACER HOY?: ") # Creamos una variable donde vamos aregistrar 
                                                 # las opcines que escoja el usuario


    if escoger_op == "1":             # aqui validamos el numero que haya ingresado el usuario si es "1"
        preguntar_agregar_mas = "si"  # esto lo coloco aqui para validar si el usuario quiere seguir agregando 
                                      # mas productos, si es "si" seguira pidiendole hasta que ingrese no 

        while preguntar_agregar_mas.lower() == "si": #Creamos un bucle while para que pueda seguir piendole lo que desea ingresar hasta que el usuario termine de ingresar productos
            print("\n INGRESE LOS DATOS")
            nombre_prod = input("Nombre del producto: ") # solicitamos los datos a registrar
            precio_prod = float(input("Precio: "))
            cantidad_prod = int(input("Cantidad: "))

            servicios.agrega_producto(inventario, nombre_prod, precio_prod, cantidad_prod) #aqui llamamos al archivo y llamamos unicamente a la funcion para agregar productos
             #lo que hace la linea 38 es le enviamos el inventario a la funcion, con los datos que el usuario ingreso, para que en el otro archivo se ejecute todo la parte logica y me de vuelta una respuesta, y automaticamente tambien se guarda en nuestra lista "inventario"
            preguntar_agregar_mas = input("¿Quiere seguir agregando? si/no: ") # aqui pedimos si desea agregar mas productos 
            print("¡GUARDADO EXITOSAMENTE!")#y un mensaje para validar que si se guardo, como un aviso

    elif escoger_op == "2":
        servicios.mostrar_inventario(inventario) #llamamos al archivo donde estan nuestras funciones y llamamos a nuestrafuncios inventario,, donde le mandamos el inventario que se tiene en este archivo
        
    elif escoger_op == "3":
        buscar_prod = input("Inrgrese el nombre del producto: ")# creamos una variable donde va tener lo que ingrese el usuario

        resultado = servicios.buscar_producto(inventario, buscar_prod) # creamos una variable donde va tener lo que me envie la funcion buscar producto
                                                                       #esto lo hacemos para visualizar lo que me envien. Al igual le mando el inventario y lo que escriba el usuario 

        if resultado:
          print("Producto encontrado:") 
          print(resultado)  #si lo encontró, mandamos un mensaje de encontrado
        else:
          print("Producto no encontrado") #si no se ecuentra, muestra esto:

    elif escoger_op == "4": 
        nombre_act = input("Ingrese el nombre del producto a actualizar: ")  
        nuevo_precio = float(input("Nuevo precio: "))                        #creamos variables para guardas los datos que ingresen, con float para escribir decimales y int enteros
        nueva_cantidad = int(input("Nueva cantidad: "))

        actualizado = servicios.actualizar_producto(inventario, nombre_act, nuevo_precio, nueva_cantidad) # le mandamos a la funcion los datos junto al inventario y colocamos todo en una variable para cuando me envien 
                                                                                                           # una respuesta se pueda visualizar

        if actualizado:       #aqui  llamamos a la variable donde recibe todo lo que recibio la funcion
          print("Producto actualizado correctamente")  # si se actualiza, si se encontro el nomnbre del producto
        else:
          print("Producto no encontrado") #por si no se encuentra el producto
    
    elif escoger_op == "5":
       producto_eliminar = input("Ingrese el nombre del producto a eliminar: ") # aqui creamos una variable para guardar el nombre del producto que quiere eliminar 

       eliminar = servicios.eliminar_producto(inventario,producto_eliminar) # creamos una variable que contenga la funcion, y en esta funcion le enviamos 
                                                #el inventario y el la varible que contiene lo que ingreso el usuario

       if eliminar: #aqui es si fue true el resultado final me enviar que fue eliminado
        print("Producto eliminado correctamente")
       else:
        print("Producto no encontrado") #si fue false no se encontró 

    elif escoger_op == "6":
      unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock = servicios.calcular_estadisticas(inventario)
      # Llamamos a la función que calcula las estadísticas del inventario y le mandamos el inventario
      # Esta función va a devolver, total de unidades, valor total del inventario
      #producto más caro y producto con mayor stock 

      print("\n--- ESTADÍSTICAS ---")                      #cuando ya haya terminado la ejecucion de todos los datos, nos los envian
                                                           #y lo que quedaría sería unicamente imprimir los resultados
      print(f"Unidades totales: {unidades_totales}")
      print(f"Valor total del inventario: {valor_total}")

      if producto_mas_caro: 
      # Verifica si existe un producto más caro
      # Esto evita errores si el inventario está vacío
        print(f"Producto más caro: {producto_mas_caro['nombre']} - Precio: {producto_mas_caro['precio']}")
        # Muestra el nombre y el precio del producto más caro
        # producto_mas_caro es un diccionario, por eso usamos ["nombre"] y ["precio"]
      if producto_mayor_stock:
        # Verifica si existe un producto con mayor stock
        print(f"Producto con mayor stock: {producto_mayor_stock['nombre']} - Cantidad: {producto_mayor_stock['cantidad']}")
        # Muestra el nombre del producto con más unidades y cuántas tiene

    elif escoger_op == "7":
        ruta = input("Ingrese el nombre del archivo para guardar (ej: archivodeinventarios.csv): ") 
        #pedimos nombre del archivo a guardar, es donde se guardará todo los datos que ingresemos
        archivos.guardar_archivo_csv(inventario, ruta) #llamamos a archivos y llamamos la funcion guardar_Archivos, le mandamos el 
                                                    # inventario y el nombre que ingrese 

    elif escoger_op == "8":
        ruta = input("Ingrese el nombre del archivo, donde tienes tus datos (ejemplo: inventario.csv): ")
        # Le pedimos al usuario el nombre del archivo
        # Ejemplo: inventario.csv

        nuevos_datos, errores = archivos.cargar_csv(ruta)
        #Llamamos a la función cargar_csv, que básicamente lee el archivo que el usuario escribió 
        # y revisa todo lo que tiene dentro. Esa función devuelve dos cosas, nuevos_datos
        # que es una lista con los productos que sí estaban bien y se pudieron cargar, y errores
        # que es la cantidad de filas que estaban mal y se ignoraron. 
        # Por ejemplo, nuevos_datos puede tener productos como arroz, leche, etc. 
        # y errores puede ser 2 si había dos líneas incorrectas en el archivo 

        if len(nuevos_datos) == 0: #si no se carga ningun archivo valido
            print("No se cargaron datos.")
        else: #pero si se carga 
              # Le preguntamos al usuario qué quiere hacer:
              # "si" → borrar todo lo anterior y usar lo nuevo
              # "no" → mezclar lo nuevo con lo que ya existe
            decision = input("¿Sobrescribir (reemplazar por algo nuevo) inventario actual? (si/no): ")

            if decision.lower() == "si": #convierte el texto a minúscula para que funcione aunque escriban en mayuscula o minuscula
                inventario = nuevos_datos
            # Sobrescribir esto borra el inventario actual y lo reemplaza por los datos del archivo
                print("Inventario reemplazado.")

            else:
                  # Si el usuario no quiere sobrescribir, entonces los unimos
                for nuevo in nuevos_datos:  # Recorremos cada producto nuevo que viene del archivo
                    existe = servicios.buscar_producto(inventario, nuevo["nombre"])
                    #Buscamos si ese producto ya existe, llamamos a la funcion de servios buscar productos en el inventario actual
                    # Puede devolver el producto si existe o none si no existe

                    if existe: # en dado caso que exista en el inventario
                        existe["cantidad"] += nuevo["cantidad"]
                           # Sumamos las cantidades de los que ya existe y de lo nuevo y lo sumamos
                        existe["precio"] = nuevo["precio"]
                        #actualizamos el precio con el nuevo valor

                    else: # si el producto no existe
                        inventario.append(nuevo) #lo agregamos al diccionario

                print("Inventario fusionado.")#mostramos un mensaje que todo fue incorporado

            print(f"Productos cargados: {len(nuevos_datos)}") #cuantos productos validos se cargaron 
            print(f"Filas inválidas omitidas: {errores}") #cuantas filas estaban malas y cuantas se ignoraron 

    elif escoger_op == "9":  
        print("Saliendo del programa...")  # aqui cambiamos el activador a false, para que cierre el ciclo
        activador = False

    else:
        print("OPCION INVALIDA, SOLO INGRESE NUMEROS DEL 1 AL 9") #por si ingresa otros numeros que no se encuentran