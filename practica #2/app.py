from flask import Flask, request

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def usuarios():
    user_id = request.args.get('id')
    if user_id:
        return f"El id del usuario es {user_id}"
    else:
        return "Lista de todos los usuarios"

if __name__ == '__main__':
    app.run(debug=True)

