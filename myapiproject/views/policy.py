from flask import request
from flask_smorest import Blueprint, abort
from myapiproject.models import PolicysTable, PlansTable, FundsTable
from myapiproject import db
from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from myapiproject.schema import PolicySchema,CompletePolicySchema,PlanSchema,ActualPolicySchema


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

    @policyblp.arguments(PolicySchema)
    @policyblp.response(201, PolicySchema)
    def post(self, policy_data): # CREATE POLICY
        #policy_data = request.get_json()
        print(policy_data)

        policy = PolicysTable(**policy_data)
        db.session.add(policy)
        db.session.commit()    

        return policy
    
    @policyblp.response(200, PolicySchema(many=True))
    def get(self): #GET all policies
        policys = PolicysTable.query.all()
        print(policys)
        return policys



@policyblp.route("/policy/<int:policy_id>")
class Policy_Read_Update_Views(MethodView):

    @policyblp.response(200, ActualPolicySchema)
    def get(self, policy_id): # GET/Read one policy
        print(type(policy_id),policy_id)
        #policy = PolicysTable.query.get_or_404(policy_id)

        # 1st Way
        #policy = db.session.query(PolicysTable, PlansTable).join(PlansTable, PolicysTable.PolicyId==PlansTable.PolicyId).filter(PolicysTable.PolicyId==policy_id).all()
        # .join(FundsTable, PolicysTable.PolicyId==FundsTable.PolicyId).
        #print(policy[0][0].PolicyId)
        #plans = []
        #for n in range(len(policy)):
        #    plans.append(policy[n][1])
        #policys = {"policy" : policy[0][0], "plans":plans}
        #-------------------
        #print(policys)

        # 2nd ways
        policy = PolicysTable.query.get_or_404(policy_id)
        plans = PlansTable.query.filter_by(PolicyId=policy_id).order_by(PlansTable.PlanType).all()
        funds = FundsTable.query.filter_by(PolicyId=policy_id).all()

        print(policy)
        print(plans)
        print(funds)

        print(policy.PolicyId)

        Policy_complete = {"PolicyID": policy.PolicyId, "ProductName":policy.ProductName, 
                           "PolicyHolder": policy.PolicyHolder, "LifeInsured": policy.LifeInsured,
                           "Nominee":policy.Nominee, "PremiumAmount":policy.PremiumAmount, 
                           "CoverageStartDate":policy.CoverageStartDate,
                           "CoverageEndDate": policy.CoverageEndDate, "FundIndicator":policy.FundIndicator,                           
                            "plans":plans, "funds":funds}
        return Policy_complete
    

    @policyblp.arguments(PolicySchema)
    @policyblp.response(200, PolicySchema)
    def put(self, policy_data, policy_id): #Create policy
        #policy_data = request.get_json()
        #print(policy_data)

        policy = PolicysTable.query.get_or_404(policy_id)
        
        policy = PolicysTable(**policy_data)
        db.session.add(policy)
        db.session.commit()
        return policy


    def delete(self, policy_id): # GET/Read one policy
        #print(policy_id)
        policy = PolicysTable.query.get_or_404(policy_id)

        db.session.delete(policy)
        db.session.commit()
        return {"message":f"Policy is deleted"}
    

    


""""
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
