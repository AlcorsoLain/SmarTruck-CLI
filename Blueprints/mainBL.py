from flask import Blueprint

main_Blueprint = Blueprint('main_blueprint', __name__)

@main_Blueprint.route('/')
def index():
    return "Hola mundo"