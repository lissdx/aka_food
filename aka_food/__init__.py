"""Initialize Flask app."""
from flask import Flask
from config import config


def create_app(config_name: str = None):
    if config_name is None or config_name not in config.keys():
        print(f"Unknown config name. Set config to default: {config['default']}")
        config_name = 'default'

    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config[config_name])
    # assets = Environment()
    # assets.init_app(app)

    with app.app_context():
        from aka_food.api.v1 import api_v1
        app.register_blueprint(api_v1.bpv)

        return app
