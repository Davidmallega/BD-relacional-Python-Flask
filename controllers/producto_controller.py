from flask import render_template, request, redirect, url_for, flash
from models.producto_model import ProductoModelo

def mostrar_formulario_producto():
    return render_template('formulario_producto.html')

def guardar_producto():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']

    if not nombre or not precio:
        flash('El nombre y el precio son obligatorios.')
        return redirect(url_for('mostrar_formulario_producto'))
    
    try:
        ProductoModelo.guardar_producto(nombre, descripcion, precio)
        flash('Producto guardado exitosamente.')
    except Exception as e:
        flash(f'Ocurrió un error: {e}')
    
    return redirect(url_for('mostrar_formulario_producto'))

def listar_productos():
    productos = ProductoModelo.obtener_productos()
    return render_template('lista_productos.html', productos=productos)

def eliminar_producto(producto_id):
    try:
        ProductoModelo.eliminar_producto(producto_id)
        flash('Producto eliminado exitosamente.', 'success')
    except Exception as e:
        flash(f'Ocurrió un error al eliminar el producto: {e}', 'error')
    
    return redirect(url_for('productos'))

def mostrar_formulario_editar_producto(producto_id):
    producto = ProductoModelo.obtener_producto_por_id(producto_id)
    return render_template('editar_producto.html', producto=producto)

def actualizar_producto(producto_id):
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']

    if not nombre or not precio:
        flash('El nombre y el precio son obligatorios.')
        return redirect(url_for('editar_producto', producto_id=producto_id))
    
    try:
        ProductoModelo.actualizar_producto(producto_id, nombre, descripcion, precio)
        flash('Producto actualizado exitosamente.')
    except Exception as e:
        flash(f'Ocurrió un error: {e}')
    
    return redirect(url_for('productos'))
