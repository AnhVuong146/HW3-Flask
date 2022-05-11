from flask import Flask

my_obj = Flask(__name__)
my_obj.config.from_mapping(SECRET_KEY = 'AnhVuong')

from app import routes
