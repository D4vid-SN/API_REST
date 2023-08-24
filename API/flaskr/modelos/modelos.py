from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class cancion(db.Model):
    id = db.Column(db.Integer, primay_key = True)
    titulo = db.Column(db.string(128))
    minutos = db.Columnc(db.Integer)
    segundos = db.Columnc(db.Integer)
    interprete = db.Columnc(db.String(128))

    def __repr__(self):
    return "{}-{}-{}-{}".format(*args: self.titulo, self.minutos, self.interprete)