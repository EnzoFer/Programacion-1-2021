from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'bolson uno': 'Combo1'},
    2: {'bolson dos': 'Combo2'},
    3: {'bolson tres': 'Combo3'},
}


class Bolsones(Resource):
    def get(self):
        return BOLSONES


class Bolson(Resource):
    def get(self, id):
        if int(id) in BOLSONES:
            return BOLSONES[int(id)]
        return "", 404











