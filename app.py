from flask import Flask, jsonify, request

# Crear la instancia principal de Flask
app = Flask(__name__)

# Ruta de inicio
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Flask API en funcionamiento correctamente",
        "status": "OK"
    })

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # Permite conexiones externas (útil en Docker o red local)
        port=8000,       # Puerto donde se ejecutará la app
        debug=True       # Recarga automática y mensajes detallados
    )
