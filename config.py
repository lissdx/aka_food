import os

# get current app's dir
app_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    FLASK_APP = "app.py"
    FLASK_RUN_HOST = os.environ.get('FLASK_RUN_HOST', "0.0.0.0")
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT', "7889")

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    FLASK_DEBUG = '1'


class DevelopmentLocalConfig(DevelopmentConfig):
    ES_HOST = os.environ.get("ES_HOST", "localhost")
    ES_PORT = os.environ.get("ES_PORT", "9200")
    HF_URL = os.environ.get("HF_URL",
                            "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2")
    HF_TOKEN = os.environ.get("HF_TOKEN")


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG', '0')


config = {
    'default': DevelopmentLocalConfig
}
