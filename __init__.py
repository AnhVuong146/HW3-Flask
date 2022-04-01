from flask import Flask

myapp_obj = Flask(__name__)
myapp_obj.config['SECRET_KEY'] = 'Anhvuong146'

from app import routes