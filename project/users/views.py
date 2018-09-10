# project/users/views.py
from flask import render_template, Blueprint, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from project import db
from project.models import User
from .forms import RegisterForm

# Blueprint config

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/login')
def login():
    return render_template('login.html')


@users_blueprint.route('/add', methods=['GET', 'POST'])
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
                return redirect(url_for('recipes.index'))
            except:
                db.session.rollback()
                flash('Error! Email ({}) already exist'.format(
                    form.email.data), 'error')
    return render_template('register.html', form=form)
