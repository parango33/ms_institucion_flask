from flask import Flask, request

from models import Schema
from service import InstitucionService


app = Flask(__name__)



@app.route('/hello')
def hello_world():
    Schema()
    return 'Hello World!'

#Create function
@app.route("/create_institucion", methods=["POST"])
def create_institucion_fun():
    return InstitucionService().create_institucion(request.get_json())


#Get insitucion function
@app.route("/institucion/<nombre>", methods=["GET"])
def get_institucion_fun(nombre):
    return InstitucionService().select_institucion(nombre)

#Get all instituciones function
@app.route("/institucion/getall", methods=["GET"])
def get_all_institucion_fun():
    return InstitucionService().select_all_instituciones()

if __name__ == '__main__':
    Schema()
    app.run(debug=True)


