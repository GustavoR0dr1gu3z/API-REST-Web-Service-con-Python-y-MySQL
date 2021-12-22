from flask import Flask, jsonify

# Nombre de mi Aplicacion
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'Mensaje': 'Bienvenido'})

# Correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)