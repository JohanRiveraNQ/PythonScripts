from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de usuarios
users = [
    {"id": 1, "name": "Usuario 1", "email": "usuario1@example.com"},
    {"id": 2, "name": "Usuario 2", "email": "usuario2@example.com"},
    {"id": 3, "name": "Usuario 3", "email": "usuario3@example.com"}
]

# Ruta para obtener todos los usuarios
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Ruta para obtener un usuario por su ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404

# Ruta para crear un nuevo usuario
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # Verificar si se proporcionó una URL en el cuerpo de la solicitud
    if 'url' in data:
        return jsonify({'error': 'No se permite incluir URLs en la solicitud'}), 400

    # Crear el usuario sin realizar solicitudes externas
    new_user = {
        "id": len(users) + 1,
        "name": data['name'],
        "email": data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Ruta para actualizar un usuario por su ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    data = request.get_json()
    user.update(data)
    return jsonify(user)

# Ruta para eliminar un usuario por su ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'Usuario eliminado'}), 200

if __name__ == '__main__':
    app.run(debug=True)
