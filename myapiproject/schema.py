from marshmallow import Schema, fields

class PolicySchema(Schema):

    PolicyID            = fields.Str(dump_only=True)
    ProductName         = fields.Str(required=True)
    PolicyHolder        = fields.Str(required=True)
    LifeInsured         = fields.Str(required=True)
    Nominee             = fields.Str(required=True)
    PremiumAmount       = fields.Float(required=True)
    CoverageStartDate   = fields.Str(required=True)
    CoverageEndDate     = fields.Str(required=True)
    FundIndicator       = fields.Boolean(required=True)


class PlanSchema(Schema):

    PlanId     = fields.Str(dump_only=True)
    PolicyId   = fields.Str(required=True)
    PlanType   = fields.Str(required=True)
    PlanName   = fields.Str(required=True)
    SumInsured = fields.Float(required=True)

class FundSchema(Schema):

    FundId              = fields.Str(dump_only=True)
    PolicyId            = fields.Str(required=True)
    FundName            = fields.Str(required=True)
    FundAmount          = fields.Float(required=True)
    FundLastPriceDate   = fields.Str(required=True)