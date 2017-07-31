from flask import Flask

import config

app = Flask(__name__)
app.config.from_object(config)

# noinspection PyUnresolvedReferences
from fridgeometer.ui import views
