# -----------------------------------------------------------------------------
# Standard Library Imports
# -----------------------------------------------------------------------------
import os
# -----------------------------------------------------------------------------
# Related Libraries Imports
# -----------------------------------------------------------------------------
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# -----------------------------------------------------------------------------
# Local Imports
# -----------------------------------------------------------------------------
from webapp.settings import DevConfig

# Must be loaded before models
app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from webapp.models import Country, PanelProvider, Location, LocationGroup, TargetGroup, LocationApi, TargetApi

def create_app(app, config_object=None):

    
    app.config.from_object(config_object)

    toolbar = DebugToolbarExtension(app)
    app.logger.debug("Debug toolbar activated")

    db.init_app(app)

    api = Api(app)
    api.add_resource(LocationApi, '/location/<int:country_code>')
    api.add_resource(TargetApi, '/target_groups/<int:country_code>')




    @app.route('/')
    def index():
        return render_template("home.html")

    return app
