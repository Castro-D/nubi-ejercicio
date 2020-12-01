from flask import Flask
from flask_restful import Api, Resource, reqparse, fields
from Modelos import db

app = Flask(__name__)
api = Api(app)

app.config.from_object('config')
db.init_app(app)
db.create_all(app=app)

encuesta_put_args = reqparse.RequestParser()
encuesta_put_args.add_argument("pregunta", type=str, help="pregunta de la encuesta", required=True)
encuesta_put_args.add_argument("respuesta1", type=str, help="respuestas de encuesta", required=True)
encuesta_put_args.add_argument("respuesta2", type=str, help="respuestas de encuesta")
encuesta_put_args.add_argument("respuesta3", type=str, help="respuestas de encuesta")
encuesta_put_args.add_argument("respuesta4", type=str, help="respuestas de encuesta")

resource_fields = {
    'id': fields.String,
    'titulo': fields.String,
    'nombre': fields.String,
    'id_pregunta': fields.String,
    'id_respuesta': fields.String,
    'pregunta': fields.String,
    'respuesta': fields.String,

}
class Encuesta(Resource):
    def get(self, encuesta_id):
        return encuestas[encuesta_id]


api.add_resource(Encuesta, "/encuesta/<int:encuesta_id>")

if __name__ == "__main__":
    app.run(debug=True)
