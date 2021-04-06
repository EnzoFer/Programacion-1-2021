import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.recursos as recursos
api = Api()

def create_app():
    app = Flask(name)
    load_dotenv()
    api.add_recursos(recursos.BolsonesRecursos,'/bolsones')
    api.add_recursos(recursos.BolsonRecursos,'/bolson/<id>')

    api.add_recursos(recursos.BolsonesPendientesRecursos, '/bolsones-pendientes')
    api.add_recursos(recursos.BolsonPendientesRecursos, '/bolson-pendientes/<id>')

    api.add_recursos(recursos.BolsonPreviosRecursos, '/bolsones-previos')

    api.add_recursos(recursos.BolsonesVentaRecursos, '/bolsones-venta')
    api.add_recursos(recursos.BolsonVentaRecursos, '/bolson-venta/<id>')

    api.add_recursos(recursos.ClientesRecursos, '/clientes')
    api.add_recursos(recursos.ClienteRecursos, '/cliente/<id>')

    api.add_recursos(recursos.ComprasRecursos, '/compras')
    api.add_recursos(recursos.CompraRecursos, '/compra/<id>')

    api.add_recursos(recursos.ProductosRecursos, '/productos')
    api.add_recursos(recursos.ProductoRecursos, '/producto/<id>')

    api.add_recursos(recursos.ProveedoresRecursos, '/proveedores')
    api.add_recursos(recursos.ProveedorRecursos, '/proveedor/<id>')









    api.init__app(app)
   return app







