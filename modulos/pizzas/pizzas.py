from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Pizza

bp_pizzas = Blueprint('pizzas', __name__, template_folder="templates")

@bp_pizzas.route('/')
def index():
    dados = Pizza.query.all()
    return render_template('pizzas.html', dados = dados)

@bp_pizzas.route('/add')
def add():
    return render_template('pizzas_add.html')

@bp_pizzas.route('/save', methods= ['POST'])
def save():
    sabor = request.form.get('sabor')
    ingredientes = request.form.get('ingredientes')
    preço = request.form.get('preço')
    
    if sabor and ingredientes and preço:
        objeto = Pizza(sabor, ingredientes, preço)
        db.session.add(objeto)
        db.session.commit()
        flash('Pizza salvo com sucesso!!!')
        return redirect('/pizzas')
    else:
        flash("Preencha todos os campos!!!")
        return redirect('/pizzas/add')


