from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class TestResource(Resource):
    def get(self):
        return {'message': 'Hello World'}

api.add_resource(TestResource, '/test')

if __name__ == '__main__':
    print("Routes:", [rule for rule in app.url_map.iter_rules()])
    app.run(debug=True, port=5001)
