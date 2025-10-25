from flask import Blueprint, jsonify
from sqlalchemy import text

from config.config_bd import engine
from models.api.user_model import Users

user_bp = Blueprint("user_bp", __name__, url_prefix="/api")


@user_bp.route("/usuarios", methods=["GET"])
def get_usuarios():
    """Obtiene todos los usuarios de la tabla 'usuarios'"""
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text(
                    "SELECT id, nombre, apellido, fechanacimiento, email, ciudad, pesoactual, tipoentrenamiento FROM usuarios")
            )
            usuarios = [
                Users(
                    id=row.id,
                    nombre=row.nombre,
                    apellido=row.apellido,
                    fechanacimiento=row.fechanacimiento,
                    email=row.email,
                    ciudad=row.ciudad,
                    pesoactual=row.pesoactual,
                    tipoentrenamiento=row.tipoentrenamiento
                ).to_dict()
                for row in result
            ]

        return jsonify({
            "status": 200,
            "message": "Usuarios obtenidos correctamente",
            "data": usuarios
        }), 200

    except Exception as e:
        print("ERROR AL CONSULTAR USUARIOS:", e)  # 👈 imprime el error real en consola
        return jsonify({"error": str(e)}), 500
