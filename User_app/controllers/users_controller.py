from User_app import app
from User_app.models.users_model import User
from flask import render_template, redirect, request

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def user_info():
    users = User.get_all()
    return render_template('read.html', users=users)

@app.route('/readone/<int:id>')
def oneuser(id):
    user = User.get_one(id)
    
    return render_template('readone.html', person=user)

@app.route('/users/new')
def create_form():
    
    return render_template('create.html')

@app.route('/create-user', methods=['POST'])
def create_user():
    
    User.create(request.form)
    
    return redirect ('/')

@app.route('/edit-user/<int:id>')
def edit_user(id):
    
    user = User.get_one(id)
    
    return render_template('edit.html', user=user)

@app.route('/edit', methods=['POST'])
def edit():
    
    User.edit(request.form)
    user_id = request.form['id']
    
    return redirect(f'/readone/{user_id}')


@app.route('/delete/<int:id>')
def delete(id):
    User.delete(id)
    
    return redirect('/')





