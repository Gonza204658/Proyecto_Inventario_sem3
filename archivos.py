def guardar_archivo_csv(inventario, ruta, incluir_header=True):
    # Esta función guarda el inventario en un archivo CSV.
    # inventario tiene las lista de productos
    # ruta es el nombre del archivo donde se va a guardar
    # incluir_header es para indicar si se escribe el encabezado


    if len(inventario) == 0: #si el inventario esta vacio no envia nada, esto valida que haya algo 
        print("No hay productos para guardar.")
        return # enviar al app.py que no hay nada y se cierra 

    try:
        archivo = open(ruta, "w")
        # Abrimos el archivo q nos dio el usuario en modo escritura ("w")
        # "w" significa que va a escribir desde cero (borra lo anterior si existe)

        # encabezado
        if incluir_header:   #aqui agregamos un encabezado para que se sepa que es cada valor
            archivo.write("nombre,precio,cantidad\n") #aqui decimos, escribe este texto en archivos

        # escribir datos
        for producto in inventario: #recorremos cada producto del inventario 
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            # Creamos una línea de texto con los datos del producto
            # Formato CSV:esto seria el encabezado nombre,precio,cantidad
            # severia algo así: arroz,2000,5
            archivo.write(linea) #escribimos esa linea en el archivo

        archivo.close() #por ultimo cerramos el documento y se guarda 

        print(f"Inventario guardado en: {ruta}") #aqui un mensaje para decirle al usuario que se guardó

    except Exception as errores: #si ocurre un error, guárdalo en una variable llamada errores
        
        print("Error al guardar el archivo:", errores)
        #Si ocurre cualquier error (por ejemplo: no se puede escribir, ruta inválida, permisos, etc.)
        #mostramos el error sin cerrar el programa

def cargar_csv(ruta): #definimos una funcion llamada cargar.csv y recivimos el nombre del archivo csv que nos envia el usuario
    inventario_cargado = []     
    # Creamos una lista vacía donde vamos a guardar los productos válidos
    # los que estén bien escritos en el archivo
    errores = 0
    # Creamos un contador de errores aquí vamos a sumar cada vez que una fila esté mal

    try:  # Intentamos ejecutar el código y si ocurre algún error (por ejemplo, el archivo no existe),
          # el programa no se va a rompe, sino que pasa al except

        with open(ruta, "r") as archivo:
            # Abrimos el archivo en modo lectura "r" y usamos "with" para que el archivo se cierre automáticamente al terminar

            encabezado = archivo.readline().strip()
            #Leemos únicamente la primera línea del archivo usando readline, 
            # que sirve para leer una sola línea, y luego aplicamos strip 
            # para eliminar los espacios y el salto de línea que viene al final. 
            # Por ejemplo, si la línea es "nombre,precio,cantidad\n", 
            # después de usar strip queda como "nombre,precio,cantidad".

            if encabezado != "nombre,precio,cantidad":
                # Validamos que el archivo tenga el encabezado correcto
                # Es decir, que la primera línea sea EXACTAMENTE esa

                print("Encabezado inválido.") #si no es mostramos un error
                return [], errores
                #Terminamos la función inmediatamente
                # y se devulve lista vacía (no se cargó nada) y errores (que en este punto es 0)

            for linea in archivo: # Recorremos cada línea del archivo (después del encabezado)
                
                partes = linea.strip().split(",")
                #Primero usamos strip para limpiar la línea, eliminando espacios y el salto de línea
                # que pueda tener al final, y luego utilizamos split(",") para dividir la línea en partes 
                # usando la coma como separador. Por ejemplo, la línea "arroz,2000,5" se transforma 
                # en una lista así: ["arroz", "2000", "5"].

                if len(partes) != 3:
                    # Verificamos que tenga exactamente 3 datos: nombre, precio, cantidad, si no lo tiene esta mal
                    errores += 1 #y aqui sumamos uno a nuestro contador
                    continue # saltamos esta linia para seguir con la otra

                nombre = partes[0] #guardamos el nombre del producto

                
                try:
                    #convertimos los datos a numero
                    precio = float(partes[1]) #convertimos a decimal en la posicion 1
                    cantidad = int(partes[2]) # covertimos a entero en la posicion 2 

                except: # Si falla la conversión (por ejemplo: "dosmil" en vez de 2000)

                    errores += 1 #suma los errores
                    continue

                if precio < 0 or cantidad < 0: #validamos que los valores no sean negativos
                    errores += 1 #sumamos error si eso pasa
                    continue #saltamos esta linea y seguimos

                producto = {   #creamos el diccionario de los productos ya limpios
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }

                inventario_cargado.append(producto) # Agregamos ese producto a la lista de productos válidos

        return inventario_cargado, errores
        # Cuando termina todo el proceso, devolvemos:
        # inventario_cargado con lista y productos buenos
        # errores con la cantidad de filas malas

    except:
        print("Error al abrir el archivo.") #si hay un error para abrir
        return [], errores #devolvemos lista vacia y errores 