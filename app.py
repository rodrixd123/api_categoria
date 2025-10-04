from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 🔗 Conexión Railway (usando pymysql)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:gzGmMybpEUnAsvoNuOeUWzefhUiDDjlN@caboose.proxy.rlwy.net:43751/railway"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo Categoría (ajustado a tu BD)
class Categoria(db.Model):
    __tablename__ = "categorias"   # 👈 nombre real de la tabla

    id_cat = db.Column(db.Integer, primary_key=True)   # 👈 campo real
    nom_cat = db.Column(db.String(100), nullable=False)  # 👈 campo real

    def to_dict(self):
        return {"id_cat": self.id_cat, "nom_cat": self.nom_cat}

# Rutas CRUD
@app.route("/categorias", methods=["GET"])
def get_categorias():
    categorias = Categoria.query.all()
    return jsonify([c.to_dict() for c in categorias])

@app.route("/categorias/<int:id_cat>", methods=["GET"])
def get_categoria(id_cat):
    categoria = Categoria.query.get(id_cat)
    if not categoria:
        return jsonify({"error": "Categoría no encontrada"}), 404
    return jsonify(categoria.to_dict())

@app.route("/categorias", methods=["POST"])
def add_categoria():
    data = request.json
    nueva = Categoria(nom_cat=data["nom_cat"])   # 👈 usamos nom_cat, no nombre
    db.session.add(nueva)
    db.session.commit()
    return jsonify(nueva.to_dict()), 201

@app.route("/categorias/<int:id_cat>", methods=["PUT"])
def update_categoria(id_cat):
    categoria = Categoria.query.get(id_cat)
    if not categoria:
        return jsonify({"error": "Categoría no encontrada"}), 404
    data = request.json
    categoria.nom_cat = data["nom_cat"]
    db.session.commit()
    return jsonify(categoria.to_dict())

@app.route("/categorias/<int:id_cat>", methods=["DELETE"])
def delete_categoria(id_cat):
    categoria = Categoria.query.get(id_cat)
    if not categoria:
        return jsonify({"error": "Categoría no encontrada"}), 404
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({"mensaje": "Categoría eliminada correctamente"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)
