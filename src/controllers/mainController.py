from flask import request
from src.services.salesService import SalesService


class MainController:
    def __init__(self):
        self.service = SalesService()

    def getSales(self, args):
        tienda = args.get('store')
        return self.service.getSalesByFilter(tienda)