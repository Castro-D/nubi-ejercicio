from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

encuestas = {}


class Encuesta(Resource):
    def get(self, encuesta_id):
        return encuestas[encuesta_id]


api.add_resource(Encuesta, "/encuesta/<int:encuesta_id>")

if __name__ == "__main__":
    app.run()
