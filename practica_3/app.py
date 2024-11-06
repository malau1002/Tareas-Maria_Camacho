# app.py
from flask import Flask
from config import Config, db
from controllers.UsuarioController import obtener_usuarios

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos con SQLAlchemy
db.init_app(app)

# Crear las tablas (solo la primera vez)
with app.app_context():
    db.create_all()

# Definir la ruta para obtener usuarios
app.route('/usuarios', methods=['GET'])(obtener_usuarios)

if __name__ == '__main__':
    app.run(debug=True)
