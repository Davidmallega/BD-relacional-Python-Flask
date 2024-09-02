from conexion import crear_conexion

class PedidoProductoModelo:
    @staticmethod
    def agregar_producto_a_pedido(pedido_id, producto_id, cantidad):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO PedidoProducto (PedidoID, ProductoID, Cantidad) VALUES (%s, %s, %s)"
            cursor.execute(consulta, (pedido_id, producto_id, cantidad))
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_productos_por_pedido(pedido_id):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = """
            SELECT Producto.Nombre, Producto.Descripción, Producto.Precio, PedidoProducto.Cantidad, Cliente.Nombre, Producto.ProductoID
            FROM PedidoProducto
            JOIN Producto ON PedidoProducto.ProductoID = Producto.ProductoID
            JOIN Pedido ON PedidoProducto.PedidoID = Pedido.PedidoID
            JOIN Cliente ON Pedido.ClienteID = Cliente.ClienteID
            WHERE PedidoProducto.PedidoID = %s
            """
            cursor.execute(consulta, (pedido_id,))
            productos = cursor.fetchall()
        conexion.close()
        print("Datos obtenidos:", productos)  # Verificación de los datos obtenidos
        return productos

    @staticmethod
    def eliminar_producto_de_pedido(pedido_id, producto_id):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM PedidoProducto WHERE PedidoID = %s AND ProductoID = %s"
            cursor.execute(consulta, (pedido_id, producto_id))
        conexion.commit()
        conexion.close()
