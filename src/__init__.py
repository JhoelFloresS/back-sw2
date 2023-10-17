from flask import Flask
from src.routes import main
from flask_cors import CORS
# Routes
# from .routes import AuthRoutes, IndexRoutes, LanguageRoutes

app = Flask(__name__)
CORS(app)

def init_app():
    # Configuration
    # app.config.from_object(config)

    # # Blueprints
    app.register_blueprint(main.main, url_prefix='/api')
    # app.register_blueprint(AuthRoutes.main, url_prefix='/auth')
    # app.register_blueprint(LanguageRoutes.main, url_prefix='/languages')

    return app