from flask import request
from flask_smorest import Blueprint, abort
from myapiproject.models import PolicysTable, PlansTable, FundsTable
from myapiproject import db
from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from myapiproject.schema import PolicySchema,CompletePolicySchema,AllPolicySchema
from flask_jwt_extended import jwt_required
import decimal


completepolicyblp = Blueprint("Complete_Policy", __name__, description="Retrive Policy with Plan and fund")


"""
Create - POST - 201   - '/policy' - Create one policy
Read - GET   -200   - '/policy'  - All policies
Read - GET   - 200  - '/policy/<integer:1>'  - Read one policies
Update - PUT    - '/policy/<integer:1>' - Update policy
Delete - DELETE - '/policy/<integer:1>' - Delete policy
"""

@completepolicyblp.route("/completePolicy/<int:policy_id>")
class Policy_Read_Update_Views(MethodView):
    
    @jwt_required()
    @completepolicyblp.response(200, CompletePolicySchema)
    def get(self, policy_id):
        """
        Get policy
        """
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


        print(policy.PremiumAmount)
        # Converting the above number into decimal  
        decimal_value = decimal.Decimal(policy.PremiumAmount)  
        # rounding off  
        rounded_number = decimal_value.quantize(decimal.Decimal('0.00'))  
        print(rounded_number)
        policy.PremiumAmount = rounded_number
        print(policy.PremiumAmount)
        Policy_complete = {"PolicyId": policy.PolicyId, "ProductName":policy.ProductName, 
                           "PolicyHolder": policy.PolicyHolder, "LifeInsured": policy.LifeInsured,
                           "Nominee":policy.Nominee, "PremiumAmount":policy.PremiumAmount, 
                           "CoverageStartDate":policy.CoverageStartDate,
                           "CoverageEndDate": policy.CoverageEndDate, "FundIndicator":policy.FundIndicator,                           
                            "plans":plans, "funds":funds}
        return Policy_complete








'''



@policyblp.route("/policy")
class PolicyViews(MethodView):

    @jwt_required()
    @policyblp.arguments(PolicySchema)
    @policyblp.response(201, PolicySchema)
    def post(self, policy_data):
        """
        Create Policy
        """ 
        #policy_data = request.get_json()
        print(policy_data)
        
        
        policy = PolicysTable(**policy_data)
        db.session.add(policy)
        db.session.commit()    
        
        return policy

    
    @jwt_required()
    @policyblp.response(200, AllPolicySchema)
    def get(self):
        """
        Get All policies
        """

        policys = PolicysTable.query.all()

        all_policies = []
        for policy in policys:
            #print(policy.PolicyId)
            policy = PolicysTable.query.get_or_404(policy.PolicyId)
            plans = PlansTable.query.filter_by(PolicyId=policy.PolicyId).order_by(PlansTable.PlanType).all()
            funds = FundsTable.query.filter_by(PolicyId=policy.PolicyId).all()
            for fund in funds:
                print(f"printing funds {fund.FundAmount}")

            Policy_complete = {"PolicyId": policy.PolicyId, "ProductName":policy.ProductName, 
                           "PolicyHolder": policy.PolicyHolder, "LifeInsured": policy.LifeInsured,
                           "Nominee":policy.Nominee, "PremiumAmount":policy.PremiumAmount, 
                           "CoverageStartDate":policy.CoverageStartDate,
                           "CoverageEndDate": policy.CoverageEndDate, "FundIndicator":policy.FundIndicator,                           
                            "plans":plans, "funds":funds}
            all_policies.append(Policy_complete)

        print(all_policies)
        {"timestamp": "abc", "Policies" : all_policies}
        return {"policies" : all_policies}



@policyblp.route("/policy/<int:policy_id>")
class Policy_Read_Update_Views(MethodView):
    
    @jwt_required()
    @policyblp.response(200, CompletePolicySchema)
    def get(self, policy_id):
        """
        Get policy
        """
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


        print(policy.PremiumAmount)
        # Converting the above number into decimal  
        decimal_value = decimal.Decimal(policy.PremiumAmount)  
        # rounding off  
        rounded_number = decimal_value.quantize(decimal.Decimal('0.00'))  
        print(rounded_number)
        policy.PremiumAmount = rounded_number
        print(policy.PremiumAmount)
        Policy_complete = {"PolicyId": policy.PolicyId, "ProductName":policy.ProductName, 
                           "PolicyHolder": policy.PolicyHolder, "LifeInsured": policy.LifeInsured,
                           "Nominee":policy.Nominee, "PremiumAmount":policy.PremiumAmount, 
                           "CoverageStartDate":policy.CoverageStartDate,
                           "CoverageEndDate": policy.CoverageEndDate, "FundIndicator":policy.FundIndicator,                           
                            "plans":plans, "funds":funds}
        return Policy_complete
    

    @jwt_required()
    @policyblp.arguments(PolicySchema)
    @policyblp.response(200, PolicySchema)
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
'''
