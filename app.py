from flask import Flask
from flask_restful import Resource, Api
from resource.hotel import Hoteis, Hotel

#pip freeze -> Para saber quais pacotes instalados

app = Flask(__name__)
api = Api(app)


api.add_resource(Hoteis, "/hoteis")
api.add_resource(Hotel, "/hoteis/<int:hotel_id>")

if __name__ == '__main__':
    app.run(debug=True)

