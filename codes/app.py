from flask import Flask, jsonify, request

app = Flask(__name__)

musicas = [
    {
        "cantor" : "Charlie Brown Jr",
        "música" : "Dia azul"
    },
    {
        "cantor" : "Charlie Brown Jr",
        "música" : "Dias de luta, dias de glória"
    }
]

# Get
@app.route('/')
def obter_musicas():
    return jsonify(musicas)

# Get com id
@app.route('/musicas/<int:indice>', methods=['GET'])
def obter_musica_com_id(indice):
    return jsonify(musicas[indice])

# POST criar novas músicas
@app.route('/', methods=['POST'])
def criar_musicas():
    nova_musica = request.get_json()
    musicas.append(nova_musica)
    return jsonify(musicas, 200)

# PUT editar música
@app.route('/musicas/<int:indice>', methods=['PUT'])
def editar_musica(indice):
    try:
        if musicas[indice] is not None:
            musica_alterada = request.get_json()
            musicas[indice] = musica_alterada
            return jsonify(musicas[indice], 200)
    except:
        return jsonify('Não foi possível editar a música!', 404)

# DELETE excluir música
@app.route('/musicas/<int:indice>', methods=['DELETE'])
def excluir(indice):
    try:
        if musicas[indice] is not None:
            del musicas[indice]
            return jsonify('Música deletada com sucesso!', 200)
    except:
        return jsonify('Não foi possível excluir a música!', 404)

app.run(port=5000, host='localhost', debug=True)