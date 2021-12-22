from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Nombre de mi Aplicacion
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ico:@localhost/bd_flask'

# Mensaje de Bienvenida
@app.route('/', methods=['GET'])
def in dex():
    return jsonify({'Mensaje': 'Bienvenido al Tutorial API'})

# Correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)