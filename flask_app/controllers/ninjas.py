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

@app.route('/dojos/<int:dojo_id>/delete')
def delete_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    Dojo.delete_dojo(data)
    return redirect('/')

@app.route('/dojos/<int:dojo_id>/edit')
def edit_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    dojo = Dojo.get_dojo_by_id(data)
    return render_template('edit_dojo.html', dojo = dojo)

@app.route('/dojos/<int:dojo_id>/update', methods=['POST'])
def update_dojo(dojo_id):
    data = {
        'id': dojo_id,
        'name': request.form['dojo_name'],
        'location': request.form['dojo_location']
    }
    Dojo.update_dojo(data)
    return redirect('/')

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect('/')

@app.route('/dojos/<int:dojo_id>')
def dojo_info(dojo_id):
    data = {
        'id': dojo_id
    }
    dojo = Dojo.get_dojo_by_id(data)
    return render_template('dojo_info.html', dojo = dojo)