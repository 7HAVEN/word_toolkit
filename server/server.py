from flask_restful import Api, Resource
from flask import Flask, request
from core.Extractive import Extractive
app = Flask(__name__)
api = Api(app)


class Server:
    def __init__(self):
        pass

    def start(self, Debug=True) -> None:
        app.run(debug=Debug)


class Response(Resource):
    def get(self):
        return {"data": "you are great"}

    def post(self):
        data = request.form['text']
        res = Extractive()
        return{"text": res.summarize(data)}


api.add_resource(Response, "/")


if __name__ == '__main__':
    app.run(debug=True)
