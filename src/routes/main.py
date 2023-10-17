from flask import Blueprint, request
from src.controllers.mainController import MainController

main = Blueprint('main_blueprint', __name__)
main_controller = MainController()




@main.route('/sales', methods=['GET'])
def hello():
    return main_controller.getSales(request.args)


@main.route('/properties', methods=['GET'])
def properties():
    return main_controller.properties()