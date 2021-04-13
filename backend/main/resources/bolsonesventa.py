from flask_restful import Resource
from flask import request

BOLSONESVENTA = {
    1: {'bolson venta': 'Bolson1'},
    2: {'bolson venta': 'Bolson2'},
    3: {'bolson venta': 'Bolson3'},
}


class BolsonesVenta(Resource):
    def get(self):
        return BOLSONESVENTA


class BolsonVenta(Resource):
    def get(self, id):
        if int(id) in BOLSONESVENTA:
            return BOLSONESVENTA[int(id)]
        return "", 404