from flask import Flask, jsonify

# Nombre de mi Aplicacion
app = Flask(__name__)


@app.route('/', methods=['GET'])
def in dex():
    return jsonify({'Mensaje': 'Bienvenido al Tutorial API'})

# Correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)