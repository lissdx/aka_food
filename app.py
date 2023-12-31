from logging.config import dictConfig
from aka_food import create_app
import os

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

VER = "29122023"

app = create_app(os.environ.get('AKAFOOD_ENV', None))

app.config['VERSION'] = VER

if __name__ == "__main__":
    print("Starting Spook: \n"
          f"VER: {VER}\n"
          f"FLASK_RUN_HOST: {app.config['FLASK_RUN_HOST']}\n"
          f"FLASK_RUN_PORT: {app.config['FLASK_RUN_PORT']}\n"
          f"FLASK_DEBUG: {app.config['FLASK_DEBUG']}\n")
    app.run(host=app.config['FLASK_RUN_HOST'], port=app.config['FLASK_RUN_PORT'], debug=app.config['FLASK_DEBUG'])
