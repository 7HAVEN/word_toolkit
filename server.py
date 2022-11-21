from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
data = {}


class Response(Resource):
    def get(self):
        return {"data": "you are great"}

    def post(self, data):
        print(request.form)
        return


api.add_resource(Response, "/")
if __name__ == '__main__':
    app.run(debug=True)
