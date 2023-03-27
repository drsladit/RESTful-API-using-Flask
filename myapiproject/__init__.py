from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from myapiproject.blocklist import Blocklist
from flask_migrate import Migrate
from flask_smorest import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Configurations
# In case of any exception in extension of flask(like Flask smorest, flask SQLalchemy).It will propagte to the flask app
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "REST API - Policy Plans Funds" # Sets Flask documentation Name
app.config["API_VERSION"] = "v1"            # Version this is also shown in Documentation name
app.config["OPENAPI_VERSION"] = "3.0.2"     # Standared for flask smorest
app.config["OPENAPI_URL_PREFIX"] = '/'      # Tells where root of API is
# API documendation configurations. These decalares to use swagger-ui for documentations
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui" # Document_URL: http://127.0.0.1:5000/swagger-ui
# place where code is available which designs our API documentation
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
# Database location to create
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABSE_URL", "sqlite:///data.db") 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config ['JSON_SORT_KEYS'] = False


# Initialising Database and migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

# Connects flask smorest to flask app
api = Api(app)

# ************* Registering blueprints to API***********
from myapiproject.views.policy import policyblp
from myapiproject.views.plans import planblp
from myapiproject.views.funds import fundblp
from myapiproject.views.user import userblp
from myapiproject.views.completePolicy import completepolicyblp

# Note: Here we register Bluprints to API but not to app(which we do for Web application)
api.register_blueprint(completepolicyblp)
api.register_blueprint(policyblp)
api.register_blueprint(planblp)
api.register_blueprint(fundblp)
api.register_blueprint(userblp)


# Below secret key helps us to identify access token sent by client is actually created by this app or not.
# The app when sending the access token for each user. It will include below S K as well in access token
app.config["JWT_SECRET_KEY"] = "aditya"
jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in Blocklist

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (
        jsonify(
            {"description": "The token has been revoked.", "error": "token_revoked"}
        ),
        401,
    )


@jwt.expired_token_loader       # Occurs when AT is expired
def expired_token_callback(jwt_header, jwt_payload):
    return (
        jsonify({"message": "The token has expired.", "error": "token_expired"}),
        401,
    )

@jwt.invalid_token_loader       # Occurs when AT is wrong
def invalid_token_callback(error):
    return (
        jsonify(
            {"message": "Signature verification failed.", "error": "invalid_token"}
        ),
        401,
    )

@jwt.unauthorized_loader       # Occurs when Bearer word is mis spelt
def missing_token_callback(error):
    return (
        jsonify(
            {
                "description": "Request does not contain an access token.",
                "error": "authorization_required",
            }
        ),
        401,
    )

@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return (
        jsonify(
            {
                "description": "The token is not fresh.",
                "error": "fresh_token_required",
            }
        ),
        401,
    )


