from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

# noinspection PyUnresolvedReferences
from fridgeometer.orm import models
# noinspection PyUnresolvedReferences
from fridgeometer.ui import views
