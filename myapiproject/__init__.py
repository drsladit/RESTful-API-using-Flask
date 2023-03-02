from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_smorest import Api


app = Flask(__name__)

# Configurations
# In case of any exception in extension of flask(like Flask smorest, flask SQLalchemy).It will propagte to the flask app
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Policy REST API" # Sets Flask documentation Name
app.config["API_VERSION"] = "v1"            # Version this is also shown in Documentation name
app.config["OPENAPI_VERSION"] = "3.0.2"     # Standared for flask smorest
app.config["OPENAPI_URL_PREFIX"] = '/'      # Tells where root of API is
# API documendation configurations. These decalares to use swagger-ui for documentations
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
# place where code is available which designs our API documentation
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
# Database location to create
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABSE_URL", "sqlite:///data.db") 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



# Initialising Database and migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

# connects flask smorest to flask app
api = Api(app)

# ************* Registering blueprints to API***********
from myapiproject.views.policy import policyblp
from myapiproject.views.plans import planblp
from myapiproject.views.funds import fundblp

# Note: Here we register Bluprints to API but not to app(which we do for Web application)
api.register_blueprint(policyblp)
api.register_blueprint(planblp)
api.register_blueprint(fundblp)