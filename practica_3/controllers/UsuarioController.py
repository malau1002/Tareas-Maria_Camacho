# controllers/UsuarioController.py
from flask import jsonify, request
from models.Usuario import Usuario
from config import db

def obtener_usuarios():
    try:
        user_id = request.args.get('id')
        if user_id:
            usuario = Usuario.query.get(user_id)
            if usuario:
                return jsonify(usuario.to_dict())
            else:
                return jsonify({'error': 'Usuario no encontrado'}), 404
        else:
            usuarios = Usuario.query.all()
            return jsonify([usuario.to_dict() for usuario in usuarios])
    except Exception as e:
        return jsonify({'error': str(e)}), 500
