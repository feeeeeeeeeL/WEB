from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Инициализация расширений
    from app.models import db
    db.init_app(app)
    
    # Регистрация блюпринтов
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.api.routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app
