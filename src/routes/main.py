from flask import Blueprint, request
from src.controllers.mainController import MainController

main = Blueprint('main_blueprint', __name__)
main_controller = MainController()




@main.route('/sales', methods=['GET'])
def hello():
    return main_controller.getSales(request)


@main.route('/properties', methods=['GET'])
def properties():
    return main_controller.properties()

@main.route('/similary', methods=['GET'])
def similary():
    return main_controller.getSimilary(request)