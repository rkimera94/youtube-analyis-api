from decouple import config
import os
from dotenv import load_dotenv
load_dotenv()


DB_DETAILS = {
    'dev': {
        'DB_TYPE': 'mysql',
        'DB_NAME': '',
        'DB_HOST': '',
        'DB_NAME': '',
        'DB_USER': '',
        'DB_PASS': ''
    },
    'source': {
        'DB_TYPE': 'postgres',
        'DB_NAME': config('DB_DATABASE_NAME'),
        'DB_HOST': config('DB_HOST'),
        'DB_USER': config('DB_USERNAME'),
        'DB_PASS': config('DB_PASSWORD'),

    },
    'target': {
        'DB_NAME': config('DB_TARGET'),
        'DB_HOST': config('DB_HOST'),
        'DB_PORT': config('DB_PORT'),
        'DB_USER': config('DB_USERNAME'),
        'DB_PASS': config('DB_PASSWORD')
    },
    'API_KEY': {
        'API_KEY': config('API_KEY'),

    },
    'BASE_url': {
        'BASE_url': config('BASE_url'),

    },
}


db_user = os.getenv("DB_USERNAME")
db_pass = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_DATABASE_NAME")


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_pass}@localhost/{db_name}"
