
from testcr import *
from flask import Flask ,request, Response, jsonify

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/',methods=["GET"])
def demo():
    return jsonify({"demo":"demogyfgd"})

@app.route('/emp1/<int:id>',methods=['GET'])
def get_emp_by_id(id):
    return_value =Office.get_emp(id)
    return jsonify(return_value)

@app.route('/emp', methods=['POST'])
def add_emp():
   request_data= request.get_json()
   print(request_data)
   Office.add_emp(request_data['name'], request_data['lastname'])
   response = Response("add emp",202, mimetype='applicaion/json')
   return response

@app.route('/emp/<int:id>', methods=['PUT'])
def update_emp():
   request_data= request.get_json()
   print(request_data)
   Office.update_emp(request_data['name'], request_data['lastname'])
   response = Response("add emp",202, mimetype='applicaion/json')
   return response


@app.route('/emp1/<int:id>',methods=['DELETE'])
def delete_emp(id):
   request_data= request.get_json()
   print(request_data)
   Office.add_emp(request_data['name'], request_data['lastname'])
   response = Response("delete emp",202, mimetype='applicaion/json')
   return response

@app.route('/stud/<int:id>',methods=['GET'])
def get_stud_by_id(id):
    return_value =Stud.get_stud(id)
    return jsonify(return_value)

@app.route('/stud', methods=['POST'])
def add_stud():
   request_data= request.get_json()
   print(request_data)
   Stud.add_stud(request_data['sname'], request_data['slastname'])
   response = Response("add stud",202, mimetype='applicaion/json')
   return response
 
if __name__ == "__main__":
    app.run(debug=True,port=8000)