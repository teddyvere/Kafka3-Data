from . import db

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    balance = db.Column(db.Integer)
    trans_id = db.Column(db.Integer, db.ForeignKey('transaction.id'))
    
    

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(250), nullable=False)
    date = db.Column(db.Integer)
    amt = db.Column(db.Integer)
    cust_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
