from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    __tablename__="courses"
    id=db.Column(db.Integer,primary_key=True)
    course_number=db.Column(db.String, nullable=False)
    course_title=db.Column(db.String, nullable =False)

class RegisteredStudent(db.Model):
    __tablename__="students"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String, nullable=False)
    grade=db.Column(db.Integer, nullable=False)
