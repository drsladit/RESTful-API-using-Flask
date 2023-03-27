from flask import request
from flask_smorest import Blueprint, abort
from myapiproject.models import FundsTable
from myapiproject import db
from sqlalchemy.exc import SQLAlchemyError
from flask.views import MethodView
from myapiproject.schema import PlainFundSchema, UpdateFundSchema
from flask_jwt_extended import jwt_required


fundblp = Blueprint("Fund", __name__, description="Operations on Funds")

"""
Create - POST - 201   - '/policy' - Create one policy
Read - GET   -200   - '/policy'  - All policies
Read - GET   - 200  - '/policy/<integer:1>'  - Read one policies
Update - PUT    - '/policy/<integer:1>' - Update policy
Delete - DELETE - '/policy/<integer:1>' - Delete policy
"""


@fundblp.route("/fund")
class Fund_Create_ViewAll(MethodView):

    @jwt_required()
    @fundblp.arguments(PlainFundSchema, description="Creates fund data")
    @fundblp.response(201, PlainFundSchema)
    def post(self, fund_data): # Create fund
        """
        Creates fund data
        """
        fund = FundsTable(**fund_data)
        db.session.add(fund)
        db.session.commit()    

        return fund
    
    @jwt_required()
    @fundblp.response(200, PlainFundSchema(many=True), description="Gives you all funds data")
    def get(self): #GET all funds
        """
        Gives you all funds data
        """
        funds = FundsTable.query.all()
        return funds



@fundblp.route("/fund/<int:fund_id>")
class Fund_Read_Update_delete_View(MethodView):

    @jwt_required()
    @fundblp.response(200, PlainFundSchema, description="Gives you fund data")
    def get(self, fund_id): # GET/Read one fund
        """
        Gives you fund data
        """
        print(fund_id)
        fund = FundsTable.query.get_or_404(fund_id)
        return fund

    @jwt_required()
    @fundblp.arguments(UpdateFundSchema, description="Updates fund data. Policy ID is mandatory in JSON body")
    @fundblp.response(200, PlainFundSchema)
    def put(self, fund_data, fund_id): #Update Fund
        """
        Updates fund data. Policy ID is mandatory in JSON body
        """
        fund = FundsTable.query.get_or_404(fund_id)
        
        fund = FundsTable(**fund_data)
        db.session.add(fund)
        db.session.commit()
        return fund

    @jwt_required()
    def delete(self, fund_id): # Delete Fund
        """
        Delete fund data.
        """
        fund = FundsTable.query.get_or_404(fund_id)

        db.session.delete(fund)
        db.session.commit()
        return {"message": f"Fund is deleted"}
