# blueprints/main.py
from flask import Blueprint, render_template

# Define the Blueprint
main_blueprint = Blueprint('main', __name__)

# Route for the landing page (Home page)
@main_blueprint.route('/')
def home():
    return render_template('landing.html')
