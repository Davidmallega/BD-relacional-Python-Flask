from conexion import crear_conexion

class ClienteModelo:
    @staticmethod
    def guardar_cliente(nombre, direccion, correo_electronico, telefono):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO Cliente (Nombre, Dirección, CorreoElectrónico, Teléfono) VALUES (%s, %s, %s, %s)"
            cursor.execute(consulta, (nombre, direccion, correo_electronico, telefono))
        conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_clientes():
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = "SELECT ClienteID, Nombre, Dirección, CorreoElectrónico, Teléfono FROM Cliente"
            cursor.execute(consulta)
            clientes = cursor.fetchall()
        conexion.close()
        return clientes
    
    @staticmethod
    def obtener_cliente_por_id(cliente_id):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = "SELECT ClienteID, Nombre, Dirección, CorreoElectrónico, Teléfono FROM Cliente WHERE ClienteID = %s"
            cursor.execute(consulta, (cliente_id,))
            cliente = cursor.fetchone()
        conexion.close()
        return cliente

    @staticmethod
    def actualizar_cliente(cliente_id, nombre, direccion, correo_electronico, telefono):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = """
            UPDATE Cliente 
            SET Nombre = %s, Dirección = %s, CorreoElectrónico = %s, Teléfono = %s
            WHERE ClienteID = %s
            """
            cursor.execute(consulta, (nombre, direccion, correo_electronico, telefono, cliente_id))
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar_cliente(cliente_id):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM Cliente WHERE ClienteID = %s"
            cursor.execute(consulta, (cliente_id,))
        conexion.commit()
        conexion.close()
