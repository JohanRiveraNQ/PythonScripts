from flask import Flask, jsonify, request
from hmac_generator import generar_hmac
import hmac



app = Flask(__name__)

# Datos de ejemplo (podrían ser datos reales almacenados en una base de datos)
productos = [
    {"id": 1, "nombre": "Producto 1", "precio": 10.0},
    {"id": 2, "nombre": "Producto 2", "precio": 20.0},
    {"id": 3, "nombre": "Producto 3", "precio": 30.0}
]

# Función para verificar la autenticidad de la solicitud mediante HMAC
def verificar_hmac(request):
    contenido = request.data
    hmac_recibido = request.headers.get('X-HMAC')

    if not hmac_recibido:
        return False
    
    hmac_calculado = generar_hmac(contenido)
    print("Contenido:", contenido)
    print("HMAC Recibido:", hmac_recibido)
    print("HMAC Generado:", hmac_calculado)
    return hmac.compare_digest(hmac_recibido, hmac_calculado)

# Ruta para obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    if not verificar_hmac(request):
        return jsonify({"mensaje": "Autenticación HMAC fallida"}), 401
    return jsonify(productos)

# Ruta para obtener un producto por su ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def obtener_producto(producto_id):
    if not verificar_hmac(request):
        return jsonify({"mensaje": "Autenticación HMAC fallida"}), 401
    
    producto = next((p for p in productos if p["id"] == producto_id), None)
    if producto:
        return jsonify(producto)
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

# Ruta para crear un nuevo producto
@app.route('/productos', methods=['POST'])
def crear_producto():
    if not verificar_hmac(request):
        return jsonify({"mensaje": "Autenticación HMAC fallida"}), 401
    
    nuevo_producto = request.json
    productos.append(nuevo_producto)
    return jsonify({"mensaje": "Producto creado exitosamente"}), 201

# Ruta para actualizar un producto existente
@app.route('/productos/<int:producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
    if not verificar_hmac(request):
        return jsonify({"mensaje": "Autenticación HMAC fallida"}), 401
    
    producto = next((p for p in productos if p["id"] == producto_id), None)
    if producto:
        datos_actualizados = request.json
        producto.update(datos_actualizados)
        return jsonify({"mensaje": "Producto actualizado exitosamente"})
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

# Ruta para eliminar un producto
@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    if not verificar_hmac(request):
        return jsonify({"mensaje": "Autenticación HMAC fallida"}), 401
    
    global productos
    productos = [p for p in productos if p["id"] != producto_id]
    return jsonify({"mensaje": "Producto eliminado exitosamente"})

# Ruta para obtener la suma de los precios de todos los productos
@app.route('/suma_precios', methods=['GET'])
def suma_precios():
    if not verificar_hmac(request):
        return jsonify({"mensaje": "Autenticación HMAC fallida"}), 401
    
    suma = sum(p["precio"] for p in productos)
    return jsonify({"suma_precios": suma})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)