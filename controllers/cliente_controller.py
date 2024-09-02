from flask import render_template, request, redirect, url_for, flash
from models.cliente_model import ClienteModelo

def mostrar_formulario():
    return render_template('formulario_cliente.html')

def guardar_cliente():
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    correo_electronico = request.form['correo_electronico']
    telefono = request.form['telefono']

    if not nombre or not correo_electronico:
        flash('El nombre y el correo electrónico son obligatorios.')
        return redirect(url_for('mostrar_formulario'))
    
    try:
        ClienteModelo.guardar_cliente(nombre, direccion, correo_electronico, telefono)
        flash('Cliente guardado exitosamente.')
    except Exception as e:
        flash(f'Ocurrió un error: {e}')
    
    return redirect(url_for('mostrar_formulario'))

def listar_clientes():
    clientes = ClienteModelo.obtener_clientes()
    return render_template('lista_clientes.html', clientes=clientes)

def eliminar_cliente(cliente_id):
    try:
        ClienteModelo.eliminar_cliente(cliente_id)
        flash('Cliente eliminado exitosamente.', 'success')
    except Exception as e:
        flash(f'Ocurrió un error al eliminar el cliente: {e}', 'error')
    
    return redirect(url_for('clientes'))

def mostrar_formulario_editar(cliente_id):
    cliente = ClienteModelo.obtener_cliente_por_id(cliente_id)
    return render_template('editar_cliente.html', cliente=cliente)

def actualizar_cliente(cliente_id):
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    correo_electronico = request.form['correo_electronico']
    telefono = request.form['telefono']

    if not nombre or not correo_electronico:
        flash('El nombre y el correo electrónico son obligatorios.')
        return redirect(url_for('editar_cliente', cliente_id=cliente_id))
    
    try:
        ClienteModelo.actualizar_cliente(cliente_id, nombre, direccion, correo_electronico, telefono)
        flash('Cliente actualizado exitosamente.')
    except Exception as e:
        flash(f'Ocurrió un error: {e}')
    
    return redirect(url_for('clientes'))

