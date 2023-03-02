from flask import request
from flask_smorest import Blueprint, abort
from myapiproject.models import FundsTable
from myapiproject import db
from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from myapiproject.schema import FundSchema


fundblp = Blueprint("Fund", __name__)

"""
Create - POST - 201   - '/policy' - Create one policy
Read - GET   -200   - '/policy'  - All policies
Read - GET   - 200  - '/policy/<integer:1>'  - Read one policies
Update - PUT    - '/policy/<integer:1>' - Update policy
Delete - DELETE - '/policy/<integer:1>' - Delete policy
"""


@fundblp.route("/fund")
class PolicyViews(MethodView):

    @fundblp.arguments(FundSchema)
    @fundblp.response(201, FundSchema)
    def post(self, fund_data): # CREATE POLICY
        #policy_data = request.get_json()
        print(fund_data)

        fund = FundsTable(**fund_data)
        db.session.add(fund)
        db.session.commit()    

        return fund
    
    @fundblp.response(200, FundSchema(many=True))
    def get(self): #GET all policies
        funds = FundsTable.query.all()
        return funds



@fundblp.route("/fund/<string:fund_id>")
class Policy_Read_Update_Views(MethodView):

    @fundblp.response(200, FundSchema)
    def get(self, fund_id): # GET/Read one policy
        print(fund_id)
        fund = FundsTable.query.get_or_404(fund_id)

        return fund
    

    @fundblp.arguments(FundSchema)
    @fundblp.response(200, FundSchema)
    def put(self, fund_data, fund_id): #Create policy
        #policy_data = request.get_json()
        #print(policy_data)

        fund = FundsTable.query.get_or_404(fund_id)
        
        fund = FundsTable(**fund_data)
        db.session.add(fund)
        db.session.commit()
        return fund


    def delete(self, fund_id): # GET/Read one policy
        #print(policy_id)
        fund = FundsTable.query.get_or_404(fund_id)

        db.session.delete(fund)
        db.session.commit()
        return {"message":f"Policy with id {fund.id} is deleted"}
