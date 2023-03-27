from flask import request
from flask_smorest import Blueprint, abort
from myapiproject.models import PolicysTable, PlansTable, FundsTable
from myapiproject import db
from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from myapiproject.schema import PlainPolicySchema,CompletePolicySchema,AllPolicySchema
from flask_jwt_extended import jwt_required
import decimal


policyblp = Blueprint("Policy", __name__, description="Operations on Policy")


"""
Create - POST - 201   - '/policy' - Create one policy
Read - GET   -200   - '/policy'  - All policies
Read - GET   - 200  - '/policy/<integer:1>'  - Read one policies
Update - PUT    - '/policy/<integer:1>' - Update policy
Delete - DELETE - '/policy/<integer:1>' - Delete policy
"""



@policyblp.route("/policy")
class PolicyViews(MethodView):

    @jwt_required()
    @policyblp.arguments(PlainPolicySchema)
    @policyblp.response(201, PlainPolicySchema)
    def post(self, policy_data):
        """
        Create Policy
        """ 
        print(policy_data)

        policy = PolicysTable(**policy_data)
        db.session.add(policy)
        db.session.commit()    
        
        return policy

    
    @jwt_required()
    @policyblp.response(200, PlainPolicySchema(many=True))
    def get(self):
        """
        Get All policies
        """
        policys = PolicysTable.query.all()
        return policys



@policyblp.route("/policy/<int:policy_id>")
class Policy_Read_Update_Views(MethodView):
    
    @jwt_required()
    @policyblp.response(200, PlainPolicySchema)
    def get(self, policy_id):
        """
        Get policy
        """
        print(type(policy_id),policy_id)
        policy = PolicysTable.query.get_or_404(policy_id)

        return policy
    

    @jwt_required()
    @policyblp.arguments(PlainPolicySchema)
    @policyblp.response(200, PlainPolicySchema)
    def put(self, policy_data, policy_id): 
        """
        Update Policy
        """
        policy = PolicysTable.query.get_or_404(policy_id)
        
        policy = PolicysTable(**policy_data)
        db.session.add(policy)
        db.session.commit()
        return policy


    @jwt_required()
    def delete(self, policy_id):
        """
        Delete policy
        """

        #print(policy_id)
        policy = PolicysTable.query.get_or_404(policy_id)

        db.session.delete(policy)
        db.session.commit()
        return {"message":f"Policy is deleted"}
    








""""
@jwt_required()
@policyblp.post("/policy")
def post_data(): #Create policy
    policy_data = request.get_json()
    print(policy_data)

    policy = PolicysTable(**policy_data)
    db.session.add(policy)
    db.session.commit()
    return {"policy": "received"}

@policyblp.get("/policy/<string:policy_id>")
def get_data(policy_id): # GET/Read one policy
    print(policy_id)
    policy = PolicysTable.query.get_or_404(policy_id)
    print(policy)
    return "policy"
"""
