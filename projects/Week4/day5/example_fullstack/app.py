from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://annascriven@localhost/students'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(20))
    last_name=db.Column(db.String(20))
    age=db.Column(db.Integer)
    grade=db.Column(db.String(1))

@app.route('/students', methods=['GET'])
def get_students():
    students=Student.query.all()
    student_list=[
        {'id':student.id, 'first_name':student.first_name,'last_name':student.last_name,
         'age': student.age,
         'grade':student.grade}
         for student in students]
    return jsonify(student_list)

app.run(debug=True)
    