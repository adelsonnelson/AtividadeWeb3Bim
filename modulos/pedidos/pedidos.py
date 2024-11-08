from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Pedido, Pizza, Usuario


bp_pedidos = Blueprint('pedidos', __name__, template_folder="templates")

@bp_pedidos.route('/')
def index():
    p = Pedido.query.all()
    return render_template('pedidos.html', pedidos = p)

@bp_pedidos.route('/add')
def add():
    u = Usuario.query.all()
    p = Pizza.query.all()
    return render_template('pedidos_add.html', usuarios = u, pizzas = p)

@bp_pedidos.route('/save', methods= ['POST'])
def save():
    usuario_id = request.form.get('usuario_id')
    pizza_id = request.form.get('pizza_id')
    data = request.form.get('data')
    
    if usuario_id and pizza_id and data:
        objeto = Usuario(usuario_id, pizza_id, data)
        db.session.add(objeto)
        db.session.commit()
        flash('Pedido salvo com sucesso!!!')
        return redirect('/pedidos')
    else:
        flash("Preencha todos os campos!!!")
        return redirect('/pedidos/add')


