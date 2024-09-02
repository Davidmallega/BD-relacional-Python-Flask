from flask import Flask, render_template
import controllers.cliente_controller as cliente_controller
import controllers.producto_controller as producto_controller
import controllers.pedido_controller as pedido_controller
import controllers.pedido_producto_controller as pedido_producto_controller

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ingresar_cliente')
def mostrar_formulario():
    return cliente_controller.mostrar_formulario()

@app.route('/guardar_cliente', methods=['POST'])
def guardar_cliente():
    return cliente_controller.guardar_cliente()

@app.route('/clientes')
def clientes():
    return cliente_controller.listar_clientes()

@app.route('/eliminar_cliente/<int:cliente_id>', methods=['POST'])
def eliminar_cliente(cliente_id):
    return cliente_controller.eliminar_cliente(cliente_id)

@app.route('/cliente/<int:cliente_id>/editar')
def editar_cliente(cliente_id):
    return cliente_controller.mostrar_formulario_editar(cliente_id)

@app.route('/cliente/<int:cliente_id>/actualizar', methods=['POST'])
def actualizar_cliente(cliente_id):
    return cliente_controller.actualizar_cliente(cliente_id)

@app.route('/ingresar_producto')
def mostrar_formulario_producto():
    return producto_controller.mostrar_formulario_producto()

@app.route('/guardar_producto', methods=['POST'])
def guardar_producto():
    return producto_controller.guardar_producto()

@app.route('/productos')
def productos():
    return producto_controller.listar_productos()

@app.route('/producto/<int:producto_id>/eliminar', methods=['POST'])
def eliminar_producto(producto_id):
    return producto_controller.eliminar_producto(producto_id)

@app.route('/producto/<int:producto_id>/editar')
def editar_producto(producto_id):
    return producto_controller.mostrar_formulario_editar_producto(producto_id)

@app.route('/producto/<int:producto_id>/actualizar', methods=['POST'])
def actualizar_producto(producto_id):
    return producto_controller.actualizar_producto(producto_id)

@app.route('/ingresar_pedido')
def mostrar_formulario_pedido():
    return pedido_controller.mostrar_formulario_pedido()

@app.route('/guardar_pedido', methods=['POST'])
def guardar_pedido():
    return pedido_controller.guardar_pedido()

@app.route('/pedidos')
def pedidos():
    return pedido_controller.listar_pedidos()

@app.route('/pedido/<int:pedido_id>/agregar_producto')
def mostrar_formulario_agregar_producto(pedido_id):
    return pedido_producto_controller.mostrar_formulario_agregar_producto(pedido_id)

@app.route('/pedido/<int:pedido_id>/guardar_producto', methods=['POST'])
def agregar_producto_a_pedido(pedido_id):
    return pedido_producto_controller.agregar_producto_a_pedido(pedido_id)

@app.route('/pedido/<int:pedido_id>/productos')
def listar_productos_por_pedido(pedido_id):
    return pedido_producto_controller.listar_productos_por_pedido(pedido_id)

@app.route('/pedido/<int:pedido_id>/eliminar_producto/<int:producto_id>', methods=['POST'])
def eliminar_producto_del_pedido(pedido_id, producto_id):
    return pedido_producto_controller.eliminar_producto_del_pedido(pedido_id, producto_id)

@app.route('/pedido/<int:pedido_id>/editar_estado')
def editar_estado_pedido(pedido_id):
    return pedido_controller.mostrar_formulario_editar_estado(pedido_id)

@app.route('/pedido/<int:pedido_id>/guardar_estado', methods=['POST'])
def guardar_estado_pedido(pedido_id):
    return pedido_controller.guardar_estado_pedido(pedido_id)

if __name__ == '__main__':
    app.run(debug=True)
