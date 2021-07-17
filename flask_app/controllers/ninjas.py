from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
# from ninjas import Ninjas

@app.route('/')
def index():
    dojos = Dojo.get_all_dojos()
    return render_template("index.html", dojos = dojos)

@app.route('/dojos/new')
def new_dojo():
    return render_template("new_dojo.html")

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/')