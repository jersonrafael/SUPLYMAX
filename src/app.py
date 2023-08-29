from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = os.getenv("secret_key")
CORS(app)

from routes import routes