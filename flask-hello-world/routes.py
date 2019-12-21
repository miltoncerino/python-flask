from flask import Blueprint

HELLO_WORLD = Blueprint('HELLO_WORLD', __name__)

@HELLO_WORLD.route('/', methods=['GET'])
def index_endpoint_handler():
    return 'HELLO WORLD!'

@HELLO_WORLD.route('/health', methods=['GET'])
def health_endpoint_handler():
    return 'I am healthy'