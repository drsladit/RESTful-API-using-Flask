from flask import request
from flask_smorest import Blueprint, abort
from myapiproject.models import PlansTable
from myapiproject import db
from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from myapiproject.schema import PlainPlanSchema


planblp = Blueprint("Plan", __name__, description="Operations on Plans")

"""
Create - POST - 201   - '/policy' - Create one policy
Read - GET   -200   - '/policy'  - All policies
Read - GET   - 200  - '/policy/<integer:1>'  - Read one policies
Update - PUT    - '/policy/<integer:1>' - Update policy
Delete - DELETE - '/policy/<integer:1>' - Delete policy
"""


@planblp.route("/plan")
class Plan_Create_ViewAll(MethodView):

    @planblp.arguments(PlainPlanSchema)
    @planblp.response(201, PlainPlanSchema)
    def post(self, plan_data):
        """
        Create plan
        """

        plan = PlansTable(**plan_data)
        db.session.add(plan)
        db.session.commit()    

        return plan
    
    @planblp.response(200, PlainPlanSchema(many=True))
    def get(self):
        """
        GET all plans
        """
        plans = PlansTable.query.all()
        print(plans)
        return plans



@planblp.route("/plan/<int:plan_id>")
class Plan_Read_Update_delete_View(MethodView):

    @planblp.response(200, PlainPlanSchema)
    def get(self, plan_id):
        """
        GET/Read one plan
        """
        print(plan_id)
        plan = PlansTable.query.get_or_404(plan_id)

        return plan
    

    @planblp.arguments(PlainPlanSchema)
    @planblp.response(200, PlainPlanSchema)
    def put(self, plan_data, plan_id): 
        """
        Update plan
        """

        plan = PlansTable.query.get_or_404(plan_id)
        
        plan = PlansTable(**plan_data)
        db.session.add(plan)
        db.session.commit()
        return plan


    def delete(self, plan_id):
        """
        Delete Plan
        """
        plan = PlansTable.query.get_or_404(plan_id)

        db.session.delete(plan)
        db.session.commit()
        return {"message":f"Plan is deleted"}
