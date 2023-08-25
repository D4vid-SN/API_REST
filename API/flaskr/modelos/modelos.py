from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.minutos, self.segundos, self.interprete)


class album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    year = db.Column(db.Integer)
    descripion = db.Column(db.String(128))
    medio = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.year, self.descripion, self.medio)


class usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    password = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}".format(self.nombre, self.password)


class medio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disco = db.Column(db.String(128))
    casete = db.Column(db.String(128))
    CD = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}".format(self.disco, self.casete, self.CD)
