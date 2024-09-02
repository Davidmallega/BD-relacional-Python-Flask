from flask import render_template, request, redirect, url_for, flash
from models.pedido_producto_model import PedidoProductoModelo
from models.pedido_model import PedidoModelo
from models.producto_model import ProductoModelo

def mostrar_formulario_agregar_producto(pedido_id):
    pedido = PedidoModelo.obtener_pedidos(pedido_id)
    productos = ProductoModelo.obtener_productos()
    
    pedido_info = {
        'PedidoID': pedido[0],  # ID del Pedido
        'Fecha': pedido[1],
        'Estado': pedido[2],
        'ClienteNombre': pedido[3]
    }

    return render_template('formulario_pedido_producto.html', pedido=pedido_info, productos=productos)

def agregar_producto_a_pedido(pedido_id):
    producto_id = request.form['producto_id']
    cantidad = request.form['cantidad']

    if not producto_id or not cantidad:
        flash('El producto y la cantidad son obligatorios.')
        return redirect(url_for('mostrar_formulario_agregar_producto', pedido_id=pedido_id))

    try:
        PedidoProductoModelo.agregar_producto_a_pedido(pedido_id, producto_id, cantidad)
        flash('Producto agregado al pedido exitosamente.')
    except Exception as e:
        flash(f'Ocurrió un error: {e}')
    
    # Redirigir a la lista de pedidos en lugar de volver al formulario de agregar producto
    return redirect(url_for('pedidos'))

def listar_productos_por_pedido(pedido_id):
    productos = PedidoProductoModelo.obtener_productos_por_pedido(pedido_id)
    
    if productos:
        nombre_cliente = productos[0][4] if productos[0][4] else 'Nombre no disponible'
    else:
        nombre_cliente = 'Cliente desconocido'
    
    return render_template('lista_productos_pedido.html', productos=productos, nombre_cliente=nombre_cliente, pedido_id=pedido_id)

def eliminar_producto_del_pedido(pedido_id, producto_id):
    try:
        PedidoProductoModelo.eliminar_producto_de_pedido(pedido_id, producto_id)
        flash('Producto eliminado del pedido exitosamente.')
    except Exception as e:
        flash(f'Ocurrió un error al eliminar el producto: {e}')
    
    return redirect(url_for('listar_productos_por_pedido', pedido_id=pedido_id))
