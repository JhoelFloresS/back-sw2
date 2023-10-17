from flask import request

class SalesController:
    def __init__(self, salesService):
        self.salesService = salesService

    def getSales(self):
        args = request.args
        tienda = args.get('tienda')
        categoria = args.get('categoria')
        rubro = args.get('rubro')

        return self.salesService.getSales(tienda, categoria, rubro)