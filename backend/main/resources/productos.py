from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductoModels


class Productos(Resource):
    def get(self):
        page = 1
        per_page = 10
        productos = db.session.query(ProductoModels)
        if request.get_json():
            filtro = request.get_json().items()
            for key, value in filtro:
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        productos = productos.paginate(page, per_page, True, 30)
        return jsonify({'productos': [producto.to_json() for producto in productos.items],
                        'total': productos.total,
                        'page': productos.page,
                        'pages': productos.pages
                        })

    def post(self):
        producto = ProductoModels.from_json(request.get_json())
        try:
            db.session.add(producto)
            db.session.commit()
            return producto.to_json(), 201
        except:
            return '', 404


class Producto(Resource):
    def get(self, id):
        producto = db.session.query(ProductoModels).get_or_404(id)
        return producto.to_json()

    def delete(self, id):
        producto = db.session.query(ProductoModels).get_or_404(id)
        try:
            db.session.delete(producto)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        producto = db.session.query(ProductoModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(producto, key, value)
        try:
            db.session.add(producto)
            db.session.commit()
            return producto.to_json(), 201
        except:
            return '', 404
