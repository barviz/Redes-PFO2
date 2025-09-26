
# Sistema de Gestión de Tareas con API Flask

Sistema backend que implementa una API REST para gestión de tareas con autenticación básica y base de datos SQLite

## Prerrequisitos

* Python 3.8 o superior
* pip (gestor de paquetes de Python)

## Configurar el entorno

```bash
# Instalar dependencias
pip install flask
```


## Estructura de archivos
Asegúrate de tener estos archivos en la carpeta:

```
REDES_PFO2/
├── auth.py
├── bdd.py
├── cliente.py
├── evidencia-response-API.pdf
├── README.md
├── requirements.txt
├── servidor.py
└── tareas.db
```
## Ejecutar el servidor
```bash
python servidor.py
```

## Ejecutar el cliente
```bash
python cliente.py
```

## Probar API (CONSOLA)

```
============================
 Sistema de Gestión de Tareas 
============================
1) Registro
2) Inicio de sesión
3) Tareas
4) Salir
Seleccione una opción: 1

=== Registro de Usuario ===
Usuario: user-consola
Contraseña: user-c123
OK Usuario creado exitosamente

============================
 Sistema de Gestión de Tareas 
============================
1) Registro
2) Inicio de sesión
3) Tareas
4) Salir
Seleccione una opción: 2

=== Inicio de Sesión ===
Usuario: user-consola
Contraseña: user-c123
OK Credenciales válidas
Ahora podés ver las tareas en la opción 3.

============================
 Sistema de Gestión de Tareas
============================
1) Registro
2) Inicio de sesión
3) Tareas
4) Salir
Seleccione una opción: 3

============================
1) Registro
2) Inicio de sesión
3) Tareas
4) Salir
============================
1) Registro
2) Inicio de sesión
3) Tareas
4) Salir
Seleccione una opción: 3

============================
1) Registro
2) Inicio de sesión
3) Tareas
3) Tareas
4) Salir
Seleccione una opción: 3

=== Tareas ===
<h1>Bienvenido al Sistema de Gestión de Tareas</h1>

============================
 Sistema de Gestión de Tareas
============================
1) Registro
2) Inicio de sesión
3) Tareas
4) Salir
Seleccione una opción: 4
👋 Saliendo...
```

## Probar API (POSTMAN)

### Registrar un nuevo usuario:

```bash
curl --location 'http://localhost:5000/registro' \
--header 'Content-Type: application/json' \
--data '{
    "usuario": "user-bar2",
    "contraseña": "pass-bar2"
}'
```

### Iniciar sesión:

```bash
curl --location 'http://localhost:5000/login' \
--header 'Content-Type: application/json' \
--data '{
    "usuario": "user-bar2",
    "contraseña": "pass-bar2"
}'
```

### Página de bienvenida:

```bash
curl --location 'http://localhost:5000/tareas' \
--header 'Content-Type: application/json'
```

## Colección de endpoints:

| Método |   Endpoint    |                    Body                     |
|--------|---------------|---------------------------------------------|
| POST   | `/registro`   | `{"usuario":"user","contraseña":"user123"}` |
| POST   | `/login`      | `{"usuario":"user","contraseña":"user123"}` |
| GET    | `/tareas`     |                     -                       |


## Capturas de pantalla

Ubicadas en la carpeta `/capturas`.

## Respuestas Conceptuales

### ¿Por qué hashear contraseñas?

Es importante hashear las contraseñas porque si la base de datos es compretida, los atacantes no obtienen las mismas en texto plano. Solo verían los hashes irreversibles. Los algoritmos de hash (bycrypt, SHA-256) son unidireccionales. Es computacionalmente inviable revertir el hash a la contraseña original. También porque los usuarios suelen usar las mismas contraseñas en varios lados. El hashing previene que un breach en un sistema comprometa otras cuentas del usuario.

### Ventajas de usar SQLite en este proyecto

La base de datos está embebida en la aplicación, no hay servidor separado. En un sólo archivo (tareas.db) está toda la base de datos. Esto también facilita la realización de un backup. También se crea automáticamente, su configuración es simple. Funciona en múltiples plataformas de la misma manera (Windows, Linux, macOS). Es ideal para proyectos pequeños. 