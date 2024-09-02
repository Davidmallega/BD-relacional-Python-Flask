from conexion import crear_conexion

class PedidoModelo:
    @staticmethod
    def guardar_pedido(fecha, estado, cliente_id):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO Pedido (Fecha, Estado, ClienteID) VALUES (%s, %s, %s)"
            cursor.execute(consulta, (fecha, estado, cliente_id))
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_pedidos(pedido_id=None):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            if pedido_id:
                consulta = """
                SELECT Pedido.PedidoID, Pedido.Fecha, Pedido.Estado, Cliente.Nombre 
                FROM Pedido 
                JOIN Cliente ON Pedido.ClienteID = Cliente.ClienteID
                WHERE Pedido.PedidoID = %s
                """
                cursor.execute(consulta, (pedido_id,))
                pedido = cursor.fetchone()
            else:
                consulta = """
                SELECT Pedido.PedidoID, Pedido.Fecha, Pedido.Estado, Cliente.Nombre 
                FROM Pedido 
                JOIN Cliente ON Pedido.ClienteID = Cliente.ClienteID
                """
                cursor.execute(consulta)
                pedidos = cursor.fetchall()
        conexion.close()
        return pedido if pedido_id else pedidos

    @staticmethod
    def actualizar_estado_pedido(pedido_id, nuevo_estado):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = "UPDATE Pedido SET Estado = %s WHERE PedidoID = %s"
            cursor.execute(consulta, (nuevo_estado, pedido_id))
        conexion.commit()
        conexion.close()
