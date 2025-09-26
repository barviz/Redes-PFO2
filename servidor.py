from flask import Flask, request, jsonify
from bdd import init_db, get_db, close_db, crear_usuario, verificar_usuario

app = Flask(__name__)

# configurar la base de datos con la aplicación
app.teardown_appcontext(close_db)

# variable para controlar si la base de datos ya fue inicializada
db_inicializada = False

@app.before_request
def antes_de_cada_request():
    """se ejecuta antes de cada request, inicializa la bdd si es necesario"""
    global db_inicializada
    if not db_inicializada:
        init_db()
        db_inicializada = True

@app.route('/')
def hola_mundo():
    return "Servidor Flask funcionando!"

@app.route('/registro', methods=['POST'])
def registro():
    """
    Endpoint para registro de usuarios
    JSON: {"usuario": "usuario", "contraseña": "1234"}
    """
    try:
        datos = request.get_json()
        
        # validar que se recibieron los datos necesarios
        if not datos or 'usuario' not in datos or 'contraseña' not in datos:
            return jsonify({"error": "Se requiere usuario y contraseña"}), 400
        
        usuario = datos['usuario']
        clave = datos['contraseña']
        
        # crear usuario en la base de datos
        éxito, mensaje = crear_usuario(usuario, clave)
        
        if éxito:
            return jsonify({"mensaje": mensaje}), 201
        else:
            return jsonify({"error": mensaje}), 400
            
    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint para inicio de sesión
    JSON: {"usuario": "usuario", "contraseña": "1234"}
    """
    try:
        datos = request.get_json()
        
        # validar que se recibieron los datos necesarios
        if not datos or 'usuario' not in datos or 'contraseña' not in datos:
            return jsonify({"error": "Se requiere usuario y contraseña"}), 400
        
        usuario = datos['usuario']
        clave = datos['contraseña']
        
        # verificar credenciales
        éxito, mensaje = verificar_usuario(usuario, clave)
        
        if éxito:
            return jsonify({"mensaje": mensaje}), 200
        else:
            return jsonify({"error": mensaje}), 401
            
    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

@app.route('/tareas', methods=['GET'])
def tareas():
    return "<h1>Bienvenido al Sistema de Gestión de Tareas</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)