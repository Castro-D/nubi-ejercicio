from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Preguntas(Base):
    titulo = db.Column(db.String(280))

    def __repr__(self):
        return self.titulo


class Respuestas(Base):
    nombre = db.Column(db.String(280))


class Encuestas(Base):
    id_pregunta = db.Column(db.Integer, db.ForeignKey('preguntas.id'))
    id_respuesta = db.Column(db.Integer, db.ForeignKey('respuestas.id'))
    pregunta = db.relationship('Preguntas', foreign_keys=[id_pregunta], backref=db.backref('options'))
    respuesta = db.relationship('Respuestas', foreign_keys=[id_respuesta])

    def __repr__(self):
        return self.respuesta.nombre
