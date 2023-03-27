from marshmallow import Schema, fields
import datetime as dt

class UserSchema(Schema):
    id                  = fields.Int(dump_only=True)
    username            = fields.Str(required=True)
    password            = fields.Str(required=True, load_only=True)

# Our aim is create a JSON having policy and associated plans and funds data.
# Schema represent mainly. Input and output validation
# We will input Policy, Plans and Funds seperately.
class PlainPolicySchema(Schema):
    PolicyId            = fields.Int(dump_only=True)
    ProductName         = fields.Str(required=True)
    PolicyHolder        = fields.Str(required=True)
    LifeInsured         = fields.Str(required=True)
    Nominee             = fields.Str(required=True)
    PremiumAmount       = fields.Float(required=True)
    CoverageStartDate   = fields.Date(required=True)
    CoverageEndDate     = fields.Date(required=True)
    FundIndicator       = fields.Boolean(required=True)
    class Meta:
        ordered = True

class PlainPlanSchema(Schema):

    PlanId     = fields.Int(dump_only=True)
    PolicyId   = fields.Str(required=True) # - REmoved and placed in nested schema
    PlanType   = fields.Str(required=True)
    PlanName   = fields.Str(required=True)
    SumInsured = fields.Float(required=True)
    class Meta:
        ordered = True
        #exclude = ["PlanId"]

class PlainFundSchema(Schema):

    FundId              = fields.Int(dump_only=True)
    PolicyId            = fields.Str(required=True)
    FundName            = fields.Str(required=True)
    FundAmount          = fields.Float(required=True)
    FundLastPriceDate   = fields.Date(required=True)
    class Meta:
        ordered = True

class UpdateFundSchema(Schema):

    #FundId              = fields.Int(dump_only=True)
    PolicyId            = fields.Str(required=True)
    FundName            = fields.Str(required=True)
    FundAmount          = fields.Float(required=True)
    FundLastPriceDate   = fields.Date(required=True)
    class Meta:
        ordered = True

class PlanSchema(PlainPlanSchema):
    PolicyId = fields.Int(required=True, load_only=True)

class FundSchema(PlainFundSchema):
    PolicyId = fields.Int(required=True, load_only=True)

class PolicySchema(PlainPolicySchema):
    plans = fields.List(fields.Nested(PlainPlanSchema(), dump_only=True))

class CompletePolicySchema(Schema): 

    PolicyId            = fields.Int(dump_only=True)
    ProductName         = fields.Str(required=True)
    PolicyHolder        = fields.Str(required=True)
    LifeInsured         = fields.Str(required=True)
    Nominee             = fields.Str(required=True)
    PremiumAmount       = fields.Float(required=True)
    CoverageStartDate   = fields.Date(required=True)
    CoverageEndDate     = fields.Date(required=True)
    FundIndicator       = fields.Boolean(required=True)
    plans   = fields.List(fields.Nested(PlainPlanSchema))
    funds   = fields.List(fields.Nested(PlainFundSchema))
    class Meta:
        ordered = True




class AllPolicySchema(Schema):
    timestamp = fields.DateTime(dump_default=dt.datetime.now())
    fispname = fields.Str(dump_default="ADI Insurance")
    fispnumber = fields.Float(dump_default=1234.00, rounding=2)
    responseCode = fields.Int(dump_default=200)
    responseStatusMessage = fields.Str(dump_default="Successful")
    policies = fields.List(fields.Nested(CompletePolicySchema))
    class Meta:
        ordered = True