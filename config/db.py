from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

host = "jesusespinosa.mysql.pythonanywhere-services.com"
user = "jesusespinosa"
bd = "jesusespinosa$test"
passw = "superpassword"

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{passw}@{host}/{bd}'  # Reemplaza con tus propios datos
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app.secret_key = ""

db = SQLAlchemy(app)

ma = Marshmallow(app)