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

class album(db.Model):
    id = db.Column(db.Integer, primay_key = True)
    titulo = db.Column(db.string(128))
    año = db.Columnc(db.Integer)
    descripion = db.Columnc(db.String(128))
    medio = db.Columnc(db.Medio)

    def __repr__(self):
    return "{}-{}-{}-{}".format(*args: self.titulo, self.año, self.segundos,self.interprete)

class usuario(db.Model):
    id = db.Column(db.Integer, primay_key = True)
    nombre = db.Column(db.string(128))
    contraseña = db.Columnc(db.String(128))

    def __repr__(self):
    return "{}-{}".format(*args: self.nombre, self.contraseña)

class Medio(db.Model):
    id = db.Column(db.Integer, primay_key = True)
    Disco = db.Column(db.string(128))
    Casete = db.Columnc(db.String(128))
    CD = db.Columnc(db.String(128))

    def __repr__(self):
    return "{}-{}-{}".format(*args: self.Disco, self.Casete, self.CD)