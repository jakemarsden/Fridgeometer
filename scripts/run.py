#!venv/bin/python
import config
from fridgeometer import app

app.run(host=config.SERVER_HOST, port=config.SERVER_PORT, debug=config.DEBUG)
