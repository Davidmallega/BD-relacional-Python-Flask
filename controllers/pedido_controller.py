from flask import render_template, request, redirect, url_for, flash
from models.pedido_model import PedidoModelo
from models.cliente_model import ClienteModelo

def mostrar_formulario_pedido():
    clientes = ClienteModelo.obtener_clientes()
    return render_template('formulario_pedido.html', clientes=clientes)

def guardar_pedido():
    fecha = request.form['fecha']
    estado = request.form['estado']
    cliente_id = request.form['cliente_id']

    if not fecha or not estado or not cliente_id:
        flash('Todos los campos son obligatorios.')
        return redirect(url_for('mostrar_formulario_pedido'))

    try:
        PedidoModelo.guardar_pedido(fecha, estado, cliente_id)
        flash('Pedido guardado exitosamente.')
    except Exception as e:
        flash(f'Ocurrió un error: {e}')
    
    return redirect(url_for('mostrar_formulario_pedido'))

def listar_pedidos():
    pedidos = PedidoModelo.obtener_pedidos()
    return render_template('lista_pedidos.html', pedidos=pedidos)

def mostrar_formulario_editar_estado(pedido_id):
    pedido = PedidoModelo.obtener_pedidos(pedido_id=pedido_id)

    pedido_info = {
        'PedidoID': pedido[0],
        'Fecha': pedido[1],
        'Estado': pedido[2],
        'ClienteNombre': pedido[3]
    }

    return render_template('editar_estado_pedido.html', pedido=pedido_info)

def guardar_estado_pedido(pedido_id):
    nuevo_estado = request.form['estado']
    try:
        PedidoModelo.actualizar_estado_pedido(pedido_id, nuevo_estado)
        flash('Estado del pedido actualizado exitosamente.')
    except Exception as e:
        flash(f'Ocurrió un error al actualizar el estado: {e}')
    
    return redirect(url_for('pedidos'))
