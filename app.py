from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'QualquerCoisa'
conexao = 'mysql+pymysql://alunos:cefetmg@127.0.0.1/bancodedados'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Usuario, Pizza, Pedido

from modulos.usuarios.usuarios import bp_usuario
app.register_blueprint(bp_usuario, url_prefix='/usuarios')

from modulos.pizzas.pizzas import bp_pizzas
app.register_blueprint(bp_pizzas, url_prefix='/pizzas')

from modulos.pedidos.pedidos import bp_pedidos
app.register_blueprint(bp_pedidos, url_prefix='/pedidos')

@app.route('/')
def index():
    return render_template('ola.html')