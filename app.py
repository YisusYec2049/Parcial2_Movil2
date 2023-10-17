from flask import Flask, jsonify, json
from config.db import db, ma, app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Ruta principal
@app.route('/')
def hello_world():
    return 'Hola, mundo!'

if __name__ == '__main__':
    app.run(debug=True)