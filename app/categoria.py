from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Nombre de mi Aplicacion
app = Flask(__name__)

# Conexcion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ico@localhost/bd_flask'

# Para que no salgan los errores de SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Modelo de la tabla categoria en la base de datos
class Categoria(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_nombre = db.Column(db.String(100))
    cat_descripcion = db.Column(db.String(200))

    def __init__(self, cat_nombre, cat_descripcion):
        self.cat_nombre = cat_nombre
        self.cat_descripcion = cat_descripcion


db.create_all()

# Mashmallow para serializar los datos, en este caso los datos de la tabla categoria
# Esquema categoria
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('cat_id', 'cat_nombre', 'cat_descripcion')


# GET, una sola respuesta
categoria_schema = CategoriaSchema()

# GET, multiples respuestas
categorias_schema = CategoriaSchema(many=True)

# GET
@app.route('/categoria', methods=['GET'])

def get_categories():
    # Obtener todas las categorias
    all_categories = Categoria.query.all()

    # Serializar los datos  
    result = categorias_schema.dump(all_categories)

    # Devuelve los datos en formato JSON
    return jsonify(result)


# GET por ID
@app.route('/categoria/<int:id>', methods=['GET'])

def get_category_id(id):
    # Obtener una categoria
    category_id = Categoria.query.get(id)

    return categoria_schema.jsonify(category_id)

# Mensaje de Bienvenida
@app.route('/', methods=['GET'])
def index():
    return jsonify({'Mensaje': 'Bienvenido al Tutorial API'})

# Correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)