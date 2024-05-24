from flask import Flask, jsonify, request

app = Flask(__name__)


movies = [
    {1, "Titulo": "Ciudadano Kane", "Director": "Orson Welles", "Ano": 1941,"Genero": "Drama"},
    {2, "Titulo": "Star Wars: Episodio V - El Imperio contraataca", "Director": "Irvin Kershner", "Ano": 1980,"Genero": "Ciencia Ficcion"},
    {3, "Titulo": "El señor de los anillos: El retorno del rey", "Director": "Peter Jackson", "Ano": 2003,"Genero": "Fantasia"}
]

@app.route('/')
def home():
    return ("NQ movies")

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)


@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = movies.get(movie_id)
    if movie:
        return jsonify(movie)
    else:
        return jsonify({'Mensaje': 'Pelicula no encontrada'}), 404


@app.route('/movies', methods=['POST'])
def add_movie():
    new_movie = request.json
    new_id=max(movies.keys())+1
    movies[new_id]={"Titulo": new_movie["Titulo"], "Director": new_movie["Director"], "Ano": new_movie["Ano"],"Genero": new_movie["Genero"]}
    return jsonify({'Mensaje': 'Pelicula añadida satisfactoriamente'}), 201


@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    act_movie = request.json
    if movie_id:
         movies[movie_id]={"Titulo": act_movie["Titulo"], "Director": act_movie["Director"], "Ano": act_movie["Ano"],"Genero": act_movie["Genero"]}    
         return jsonify({'Mensaje': 'Pelicula actualizada'}),200
    else: 
         return jsonify({'Mensaje': 'Pelicula no encontrada'}), 404


@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    act_movie = request.json
    if movie_id:
         movies[movie_id]={"Titulo": act_movie["Titulo"], "Director": act_movie["Director"], "Ano": act_movie["Ano"],"Genero": act_movie["Genero"]}    
         return jsonify({'Mensaje': 'Pelicula actualizada'}),200
    else: 
         return jsonify({'Mensaje': 'Pelicula no encontrada'}), 404

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    if movie_id in movies:
        del  movies[movie_id]
        return jsonify({'Mensaje': 'Pelicula eliminada'}),200
    else: 
         return jsonify({'Mensaje': 'Pelicula no encontrada'}), 404

app.run(host='0.0.0.0', port=3000)

if __name__ == '__main__':
    app.run(debug=True)



