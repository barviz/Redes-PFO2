import sqlite3
from flask import g
from auth import hash_clave, verificar_clave

# configuración de la base de datos
BDD = 'tareas.db'

def get_db():
    """obtiene la conexión a la base de datos"""
    if 'db' not in g:
        g.db = sqlite3.connect(BDD)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """cierra la conexión a la base de datos"""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """inicializa la base de datos creando las tablas necesarias"""
    db = get_db()
    
    db.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            clave_hash TEXT NOT NULL
        )
    ''')
    
    db.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            completada BOOLEAN DEFAULT FALSE,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        )
    ''')
    
    db.commit()
    print("✅ Base de datos inicializada correctamente")

def crear_usuario(usuario, clave):
    """
    crea un nuevo usuario en la base de datos
    retorna: (éxito, mensaje)
    """
    db = get_db()
    
    try:
        # verificar si el usuario ya existe
        usuario_existente = db.execute(
            'SELECT id FROM usuarios WHERE usuario = ?', (usuario,)
        ).fetchone()
        
        if usuario_existente:
            return False, "El usuario ya existe"
        
        # hashear la contraseña antes de guardar
        clave_hash = hash_clave(clave)
        
        # insertar nuevo usuario
        db.execute(
            'INSERT INTO usuarios (usuario, clave_hash) VALUES (?, ?)',
            (usuario, clave_hash)
        )
        db.commit()
        return True, "Usuario creado exitosamente"
        
    except sqlite3.Error as e:
        return False, f"Error al crear usuario: {str(e)}"

def verificar_usuario(usuario, clave):
    """
    verifica las credenciales de un usuario
    retorna: (éxito, mensaje)
    """
    db = get_db()
    
    try:
        # buscar usuario en la base de datos
        usuario_db = db.execute(
            'SELECT * FROM usuarios WHERE usuario = ?', (usuario,)
        ).fetchone()
        
        if not usuario_db:
            return False, "Usuario no encontrado"
        
        # verificar contraseña
        if verificar_clave(usuario_db['clave_hash'], clave):
            return True, "Credenciales válidas"
        else:
            return False, "Contraseña incorrecta"
            
    except sqlite3.Error as e:
        return False, f"Error al verificar usuario: {str(e)}"