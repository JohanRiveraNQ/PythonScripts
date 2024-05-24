from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/imc', methods=['POST'])
def calculate_imc():
    data = request.get_json()
    weight = data.get('weight')
    height = data.get('height')

    if not weight or not height:
        return jsonify({'error': 'Missing data'}), 400

    try:
        weight = float(weight)
        height = float(height)
    except ValueError:
        return jsonify({'error': 'Invalid data types'}), 400

    if height <= 0 or weight <= 0:
        return jsonify({'error': 'Invalid height or weight value'}), 400

    imc = weight / (height ** 2)
    return jsonify({'imc': imc})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
