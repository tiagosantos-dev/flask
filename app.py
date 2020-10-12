from flask import Flask
from flask_restful import Resource, Api
from resource.hotel import Hoteis, Hotel
from sql_alchemy import banco

#pip freeze -> Para saber quais pacotes instalados

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///banco.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def criar_banco():
    banco.create_all()

api.add_resource(Hoteis, "/hoteis")
api.add_resource(Hotel, "/hoteis/<int:hotel_id>")

if __name__ == '__main__':
    #inicializa com o banco de dados
    banco.init_app(app)
    app.run(debug=True)

