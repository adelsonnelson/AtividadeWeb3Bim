from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Pedido

bp_pedidos = Blueprint('pedidos', __name__, template_folder="templates")

@bp_pedidos.route('/')
def index():
    dados = Pedido.query.all()
    return render_template('pedidos.html', dados = dados)

@bp_pedidos.route('/add')
def add():
    return render_template('pedidos_add.html')

@bp_pedidos.route('/save', methods= ['POST'])
def save():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    
    if nome and email and senha:
        objeto = Pedido(nome, email, senha)
        db.session.add(objeto)
        db.session.commit()
        flash('Pedido salvo com sucesso!!!')
        return redirect('/pedidos')
    else:
        flash("Preencha todos os campos!!!")
        return redirect('/pedidos/add')


