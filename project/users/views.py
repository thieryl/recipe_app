# project/users/views.py
from flask import render_template, Blueprint, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from project import db
from project.models import User
from .forms import RegisterForm

# Blueprint config

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/getusers')
def get_users():
    all_users = User.query.all()
    return render_template('user.html', users=all_users)


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_user = User(form.email.data, form.password.data)
                new_user.authenticated = True
                db.session.add(new_user)
                db.session.commit()
                flash('Thanks for registering!', 'success')
                return redirect(url_for('users.get_users'))
            except IntegrityError:
                db.session.rollback()
                flash('ERROR! Email ({}) already exists.'.format(
                    form.email.data), 'error')
    return render_template('register.html', form=form)


@users_blueprint.route('/login')
def login():
    return render_template('login.html')
