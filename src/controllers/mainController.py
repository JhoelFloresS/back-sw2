from flask import request
from src.services.salesService import SalesService


class MainController:
    def __init__(self):
        self.service = SalesService()

    def getSales(self, request):
        tienda = request.args.get('store')
        return self.service.getSalesByFilter(tienda)

    def getSimilary(_, request):
        tienda = request.args.get('store')
        # print('valid')
        # print(request.args.get('store'))
        return SalesService().getSimilary(tienda)