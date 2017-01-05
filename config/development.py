import os

DEBUG = True
SECRET_KEY = '6ec0bc4d27fa09e27cc745275337e78343b32c2253b5eda94c4094b24a8f4ba3a7d7abfaacfe7649c8f3f7d447de0e78d5d431181ac72b639b2ae29a1ded6a51'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
SQLALCHEMY_ECHO = True
HOST = '0.0.0.0'
PORT = 8080
