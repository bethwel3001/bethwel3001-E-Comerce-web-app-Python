from flask import Flask
from BLUEPRINTS.login import login_bp
from BLUEPRINTS.signup import signup_bp
from BLUEPRINTS.home import home_bp
from BLUEPRINTS.landing import main_blueprint
# BLUEPRINTS
app = Flask(__name__)
# Register the main blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(home_bp)
app.secret_key="PYTHONIFY"


if __name__ == "__main__":
    app.run(debug=True)
