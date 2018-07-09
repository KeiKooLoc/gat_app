# -----------------------------------------------------------------------------
# Standard Library Imports
# -----------------------------------------------------------------------------
import os
# -----------------------------------------------------------------------------
# Related Libraries Imports
# -----------------------------------------------------------------------------
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
# -----------------------------------------------------------------------------
# Local Imports
# -----------------------------------------------------------------------------


def create_app(config_object=None):

    app = Flask(__name__)
    app.config.from_object(config_object)

    toolbar = DebugToolbarExtension(app)
    app.logger.debug("Debug toolbar activated")

    @app.route('/')
    def index():
        return render_template("home.html")

    return app
