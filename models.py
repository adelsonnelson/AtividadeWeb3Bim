from database import db

class Usuario(db.Model):
    __tablename__='usuario'
    id = db.Column(db.Integer, primary_key = True) #o Primary key torna ele auto-incremment e chava primária
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50))
    senha = db.Column(db.String(50))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):    
        return "<Usuario {}>".format(self.nome)


class Pizza(db.Model):
    __tablename__='pizza'
    id = db.Column(db.Integer, primary_key = True)
    sabor = db.Column(db.String(50))
    ingredientes = db.Column(db.String(50))
    preco = db.Column(db.Float)
    
    def __init__(self, sabor, ingredientes, preco):
        self.sabor = sabor
        self.ingredientes = ingredientes
        self.preco = preco

    def __repr__(self):
        return "<Pizza {}>".format(self.sabor)
        

class Pedido(db.Model):
    __tablename__='pedido'
    id = db.Column(db.Integer, primary_key = True) #o Primary key torna ele auto-incremment e chava primária
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    data = db.Column(db.Date)
    
    usuario = db.relationship('Usuario', foreign_keys = usuario_id)
    pizza = db.relationship('Pizza', foreign_keys = pizza_id)
    

    def __init__(self, usuario_id, pizza_id, data):
        self.usuario_id = usuario_id
        self.pizza_id = pizza_id
        self.data = data

    def __repr__(self):    
        return "<Pedido {} . {} . {}>".format(self.usuario.nome, self.pizza.sabor, self.data)