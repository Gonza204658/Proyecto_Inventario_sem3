📦 Sistema de Inventario en Python
Descripción

Este proyecto es un sistema de inventario hecho en Python que permite gestionar productos de forma sencilla desde la consola. El usuario puede agregar, buscar, actualizar, eliminar productos y también guardar o cargar la información usando archivos CSV.

El objetivo es facilitar el control de productos y practicar lógica de programación.

⚙️FUNCIONALIDADES:

El programa cuenta con un menú donde el usuario puede elegir entre varias opciones:

Agregar productos
Permite ingresar nombre, precio y cantidad de un producto.
También da la opción de seguir agregando más productos.
Mostrar inventario
Muestra todos los productos guardados.
Si no hay productos, indica que el inventario está vacío.
Buscar producto
Permite buscar un producto por su nombre.
Muestra el producto si existe o un mensaje si no se encuentra.
Actualizar producto
Permite cambiar el precio y la cantidad de un producto existente.
Eliminar producto
Elimina un producto del inventario si existe.
Estadísticas del inventario
Calcula y muestra:
Total de unidades
Valor total del inventario
Producto más caro
Producto con mayor cantidad
Guardar inventario (CSV)
Guarda todos los productos en un archivo CSV.
Cargar inventario (CSV)
Permite cargar productos desde un archivo CSV.
El usuario puede decidir si reemplaza todo el inventario o si lo fusiona con el actual.
Salir
Finaliza el programa

🗂️ Estructura del proyecto

El proyecto está dividido en varios archivos:

app.py → contiene el menú principal y la interacción con el usuario
servicios.py → contiene la lógica del inventario (agregar, buscar, actualizar, etc.)
archivos.py → maneja la lectura y escritura de archivos CSV
