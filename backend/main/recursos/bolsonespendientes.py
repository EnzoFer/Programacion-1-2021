from flask_restful import recursos
from flask import request


class BolsonesPendiente(recursos):
    def get(self, id):
        if int(id) in BolsonesPendiente:
            return BolsonesPendiente[int(id)]
        return '', 404

class BolsonPendiente(recursos):
    def get(self, id):
        if int(id) in BolsonPendiente:
            return BolsonPendiente[int(id)]
        return '', 404