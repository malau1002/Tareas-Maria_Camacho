# models/Usuario.py
from config import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String, nullable=False)
    # Añade más columnas según lo que esté definido en tu tabla `usuarios`

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            # Incluye otros campos si existen
        }
