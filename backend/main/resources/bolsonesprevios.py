from flask_restful import Resource
from flask import request

BOLSONESPREVIOS = {
    1: {'bolson previo': 'Bolson1'},
    2: {'bolson previo': 'Bolson2'},
    3: {'bolson previo': 'Bolson3'},
}


class BolsonesPrevios(Resource):
    def get(self):
        return BOLSONESPREVIOS


class BolsonPrevio(Resource):
    def get(self, id):
        if int(id) in BOLSONESPREVIOS:
            return BOLSONESPREVIOS[int(id)]
        return "", 404