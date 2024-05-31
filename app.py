from flask import Flask, jsonify, request
from flask_cors import CORS # type: ignore}
from hugging import imageClass
app = Flask(__name__)
CORS(app)

imagenn = imageClass()

@app.route('/image-page', methods=['POST'])
def imageClassi():
    data = request.get_json()
    image_url = data.get('url')
    resultado = imagenn(image_url)
    return jsonify(resultado)


xmen_data = [
    {
        "id": 1,
        "name": "Cyclops",
        "alias": "Scott Summers",
        "powers": ["Optic blasts", "Leadership"],
        "city": "Xavier's School for Gifted Youngsters",
        "first_appearance": "X-Men '97 Episode 1"
    },
    {
        "id": 2,
        "name": "Storm",
        "alias": "Ororo Munroe",
        "powers": ["Weather manipulation", "Flight"],
        "city": "Xavier's School for Gifted Youngsters",
        "first_appearance": "X-Men '97 Episode 1"
    },
    {
        "id": 3,
        "name": "Wolverine",
        "alias": "Logan",
        "powers": ["Regeneration", "Adamantium claws"],
        "city": "Xavier's School for Gifted Youngsters",
        "first_appearance": "X-Men '97 Episode 1"
    },
    {
        "id": 4,
        "name": "Rogue",
        "alias": "Anna Marie",
        "powers": ["Power absorption", "Flight"],
        "city": "Xavier's School for Gifted Youngsters",
        "first_appearance": "X-Men '97 Episode 1"
    },
    {
        "id": 5,
        "name": "Jean Grey",
        "alias": "Jean Grey",
        "powers": ["Telepathy", "Telekinesis"],
        "city": "Xavier's School for Gifted Youngsters",
        "first_appearance": "X-Men '97 Episode 1"
    }
]

@app.route('/xmen', methods=['GET'])
def get_all_xmen():
    return jsonify(xmen_data)

@app.route('/xmen/<int:xmen_id>', methods=['GET'])
def get_xmen_by_id(xmen_id):
    xmen = next((xmen for xmen in xmen_data if xmen["id"] == xmen_id), None)
    if xmen:
        return jsonify(xmen)
    else:
        return jsonify({"error": "X-Men not found"}), 404

@app.route('/xmen', methods=['POST'])
def add_xmen():
    new_xmen = request.json
    xmen_data.append(new_xmen)
    return jsonify({"message": "X-Men added successfully"}), 201

@app.route('/xmen/<int:xmen_id>', methods=['PUT'])
def update_xmen(xmen_id):
    xmen = next((xmen for xmen in xmen_data if xmen["id"] == xmen_id), None)
    if xmen:
        updated_xmen = request.json
        xmen.update(updated_xmen)
        return jsonify({"message": "X-Men updated successfully"})
    else:
        return jsonify({"error": "X-Men not found"}), 404

@app.route('/xmen/<int:xmen_id>', methods=['DELETE'])
def delete_xmen(xmen_id):
    global xmen_data
    xmen_data = [xmen for xmen in xmen_data if xmen["id"] != xmen_id]
    return jsonify({"message": "X-Men deleted successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
