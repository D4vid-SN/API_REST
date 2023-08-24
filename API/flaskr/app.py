from flask import create_app
from .modelos import db, cancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    c = cancion(titulo = 'Prueba', minutos = 2, segundos = 25, interprete =)
    db.session.add(c)
    db.session.commit()
    print(cancion.query.all())