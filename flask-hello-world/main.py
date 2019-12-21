#!/usr/bin/env python3
import os
import argparse
from flask import Flask
from routes import HELLO_WORLD

app = Flask(__name__)
app.register_blueprint(HELLO_WORLD)

def main():

    parser = argparse.ArgumentParser(prog="hello-world", add_help=False, description="just a flask hello world")
    options = parser.add_argument_group("Arguments")
    options.add_argument('--help', '-h', help="Help message", action='help')
    options.add_argument('--host', help="Host where to run health check", default="127.0.0.1", required=False)
    options.add_argument('--port', help="Port where to run health check", default="3000", required=False)
    options.add_argument('--debug', help="Debug?", action='store_true', default=True, required=False)
    args = parser.parse_args()

    app.run(debug=args.debug, host=args.host, port=args.port)

if __name__ == "__main__":
    main()