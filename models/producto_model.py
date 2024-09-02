from conexion import crear_conexion

class ProductoModelo:
    @staticmethod
    def guardar_producto(nombre, descripcion, precio):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO Producto (Nombre, Descripción, Precio) VALUES (%s, %s, %s)"
            cursor.execute(consulta, (nombre, descripcion, precio))
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_productos():
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = "SELECT ProductoID, Nombre, Descripción, Precio FROM Producto"
            cursor.execute(consulta)
            productos = cursor.fetchall()
        conexion.close()
        return productos

    @staticmethod
    def obtener_producto_por_id(producto_id):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = "SELECT ProductoID, Nombre, Descripción, Precio FROM Producto WHERE ProductoID = %s"
            cursor.execute(consulta, (producto_id,))
            producto = cursor.fetchone()
        conexion.close()
        return producto

    @staticmethod
    def actualizar_producto(producto_id, nombre, descripcion, precio):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = """
            UPDATE Producto 
            SET Nombre = %s, Descripción = %s, Precio = %s
            WHERE ProductoID = %s
            """
            cursor.execute(consulta, (nombre, descripcion, precio, producto_id))
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar_producto(producto_id):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM Producto WHERE ProductoID = %s"
            cursor.execute(consulta, (producto_id,))
        conexion.commit()
        conexion.close()
