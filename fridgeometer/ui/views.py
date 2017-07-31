from flask import render_template

from fridgeometer import app


@app.route('/')
@app.route('/index')
def get_index():
    return render_template('index.html')
