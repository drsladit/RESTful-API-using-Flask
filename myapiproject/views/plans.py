from flask import request
from flask_smorest import Blueprint, abort
from myapiproject.models import PlansTable
from myapiproject import db
from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from myapiproject.schema import PlanSchema


planblp = Blueprint("Plan", __name__)

"""
Create - POST - 201   - '/policy' - Create one policy
Read - GET   -200   - '/policy'  - All policies
Read - GET   - 200  - '/policy/<integer:1>'  - Read one policies
Update - PUT    - '/policy/<integer:1>' - Update policy
Delete - DELETE - '/policy/<integer:1>' - Delete policy
"""


@planblp.route("/plan")
class PolicyViews(MethodView):

    @planblp.arguments(PlanSchema)
    @planblp.response(201, PlanSchema)
    def post(self, plan_data): # CREATE POLICY
        #policy_data = request.get_json()
        print(plan_data)

        plan = PlansTable(**plan_data)
        db.session.add(plan)
        db.session.commit()    

        return plan
    
    @planblp.response(200, PlanSchema(many=True))
    def get(self): #GET all policies
        plans = PlansTable.query.all()
        print(plans)
        return plans



@planblp.route("/plan/<int:plan_id>")
class Policy_Read_Update_Views(MethodView):

    @planblp.response(200, PlanSchema)
    def get(self, plan_id): # GET/Read one policy
        print(plan_id)
        plan = PlansTable.query.get_or_404(plan_id)

        return plan
    

    @planblp.arguments(PlanSchema)
    @planblp.response(200, PlanSchema)
    def put(self, plan_data, plan_id): #Create policy
        #policy_data = request.get_json()
        #print(policy_data)

        plan = PlansTable.query.get_or_404(plan_id)
        
        plan = PlansTable(**plan_data)
        db.session.add(plan)
        db.session.commit()
        return plan


    def delete(self, plan_id): # GET/Read one policy
        #print(policy_id)
        plan = PlansTable.query.get_or_404(plan_id)

        db.session.delete(plan)
        db.session.commit()
        return {"message":f"Plan is deleted"}
