from flask import request
from flask_smorest import Blueprint, abort
from myapiproject.models import UserTable
from myapiproject import db
from myapiproject.blocklist import Blocklist
from flask.views import MethodView
from myapiproject.schema import UserSchema
#from passlib import pbkdf2_sha256
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt


userblp = Blueprint("User", __name__)

@userblp.route('/register')
class UserRegister(MethodView):

    @userblp.arguments(UserSchema)
    def post(self, user_data):
       
        if UserTable.query.filter(UserTable.username == user_data["username"]).first():
            abort(409, "User with this username already exists") 

        user = UserTable(
            username = user_data['username'],
            password = generate_password_hash(user_data['password'])
        )
        
        db.session.add(user)
        db.session.commit()

        return {"message":"User created successfully"}, 200

@userblp.route('/login')
class UserLogin(MethodView):

    @userblp.arguments(UserSchema)
    def post(self, user_data):
        
        user = UserTable.query.filter(UserTable.username == user_data["username"]).first()
        
        if user.username == user_data["username"] and check_password_hash(user.password, user_data['password']):
            access_token = create_access_token(identity=user.id)
            return {"access_token":access_token}
        
        abort(401, message="Invalid login")

@userblp.route('/logout')
class UserLogout(MethodView):

    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        Blocklist.add(jti)
        return {"message":"Loggedout Successfully"}

        


@userblp.route('/user/<int:user_id>')
class UserRegister(MethodView):

    @userblp.response(200, UserSchema)
    def get(self, user_id):
        user = UserTable.query.get_or_404(user_id)

        return user
    
    def delete(self, user_id):
        user = UserTable.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()

        return {"message":"User deleted"}, 200