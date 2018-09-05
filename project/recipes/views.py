# project/recipes/views.py
from flask import render_template, Blueprint

# template config
recipes_blueprint = Blueprint('recipes', __name__,
                              template_folder='templates')


@recipes_blueprint.route('/')
def indec():
    return render_template('index.html')
