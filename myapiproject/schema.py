from marshmallow import Schema, fields


class UserSchema(Schema):
    id                  = fields.Int(dump_only=True)
    username            = fields.Str(required=True)
    password            = fields.Str(required=True, load_only=True)

# Our aim is create a JSON having policy and associated plans and funds data.
# Schema represent mainly. Input and output validation
# We will input Policy, Plans and Funds seperately.
class PlainPolicySchema(Schema):
    PolicyID            = fields.Int(dump_only=True)
    ProductName         = fields.Str(required=True)
    PolicyHolder        = fields.Str(required=True)
    LifeInsured         = fields.Str(required=True)
    Nominee             = fields.Str(required=True)
    PremiumAmount       = fields.Float(required=True)
    CoverageStartDate   = fields.Date(required=True)
    CoverageEndDate     = fields.Date(required=True)
    FundIndicator       = fields.Boolean(required=True)


class PlainPlanSchema(Schema):
    class Meta:
        ordered = True
    PlanId     = fields.Int(dump_only=True)
    PolicyId   = fields.Str(required=True) # - REmoved and placed in nested schema
    PlanType   = fields.Str(required=True)
    PlanName   = fields.Str(required=True)
    SumInsured = fields.Float(required=True)


class PlainFundSchema(Schema):
    class Meta:
        ordered = True
    FundId              = fields.Int(dump_only=True)
    PolicyId            = fields.Str(required=True)
    FundName            = fields.Str(required=True)
    FundAmount          = fields.Float(required=True)
    FundLastPriceDate   = fields.Date(required=True)


class PlanSchema(PlainPlanSchema):
    PolicyId = fields.Int(required=True, load_only=True)

class FundSchema(PlainFundSchema):
    PolicyId = fields.Int(required=True, load_only=True)

class PolicySchema(PlainPolicySchema):
    plans = fields.List(fields.Nested(PlainPlanSchema(), dump_only=True))

class CompletePolicySchema(Schema):
    policy  = fields.Nested(PlainPolicySchema)
    plans   = fields.List(fields.Nested(PlainPlanSchema))
    funds   = fields.List(fields.Nested(PlainFundSchema))

class ActualPolicySchema(Schema):


    PolicyID            = fields.Int(dump_only=True)
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
    