from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

from models import User, Student

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form['username'],
            password=request.form['password']
        ).first()
        if user:
            session['user'] = user.username
            return redirect('/dashboard')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    students = Student.query.all()
    return render_template('dashboard.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student = Student(
            name=request.form['name'],
            email=request.form['email'],
            course=request.form['course']
        )
        db.session.add(student)
        db.session.commit()
        return redirect('/dashboard')
    return render_template('add_student.html')

@app.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True)