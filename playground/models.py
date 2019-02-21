from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    __tablename__="courses"
    id=db.Column(db.Integer,primary_key=True)
    course_number=db.Column(db.String, nullable=False)
    course_title=db.Column(db.String, nullable =False)

    students= db.relationship("RegisteredStudent", backref="courses",lazy=True)

    def addStudent(self, name, grade):
        newStudent= RegisteredStudent(name=name,grade=grade,course_id=self.id)
        db.session.add(newStudent)
        db.session.commit()

class RegisteredStudent(db.Model):
    __tablename__="students"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String, nullable=False)
    grade=db.Column(db.Integer, nullable=False)

    course_id=db.Column(db.Integer, db.ForeignKey('courses.id'),nullable =False)
