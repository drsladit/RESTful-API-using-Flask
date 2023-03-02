from myapiproject import db



class CustomersTable(db.Model):

    __tablename__ = "CustomersTable"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    policys = db.Column(db.String(255))


class PolicysTable(db.Model):

    __tablename__ = "PolicysTable"

    PolicyId            = db.Column(db.Integer, primary_key=True)
    ProductName         = db.Column(db.String(255), nullable=False)
    PolicyHolder        = db.Column(db.String(255), nullable=False)
    LifeInsured         = db.Column(db.String(255), nullable=False)
    Nominee             = db.Column(db.String(255), nullable=False)
    PremiumAmount       = db.Column(db.Float, nullable=False)
    CoverageStartDate   = db.Column(db.String(255), nullable=False)
    CoverageEndDate     = db.Column(db.String(255), nullable=False)
    FundIndicator       = db.Column(db.Boolean, nullable=False)

    def __init__(self, ProductName, PolicyHolder, LifeInsured, Nominee, PremiumAmount, 
                 CoverageStartDate, CoverageEndDate, FundIndicator):
        self.ProductName        = ProductName
        self.PolicyHolder       = PolicyHolder
        self.LifeInsured        = LifeInsured
        self.Nominee            = Nominee
        self.PremiumAmount      = PremiumAmount
        self.CoverageStartDate  = CoverageStartDate
        self.CoverageEndDate    = CoverageEndDate
        self.FundIndicator      = FundIndicator



class PlansTable(db.Model):

    __tablename__ = "PlansTable"

    PlanID     = db.Column(db.Integer, primary_key=True)
    PolicyId   = db.Column(db.Integer, db.ForeignKey('PolicysTable.PolicyId'), nullable=False)
    PlanType   = db.Column(db.String(255), nullable=False)
    PlanName   = db.Column(db.String(255), nullable=False)
    SumInsured = db.Column(db.Float, nullable=False)


class FundsTable(db.Model):

    __tablename__ = "FundsTable"

    FundId              = db.Column(db.Integer, primary_key=True)
    PolicyId            = db.Column(db.Integer, db.ForeignKey('PolicysTable.PolicyId'), nullable=False)
    FundName            = db.Column(db.String(255), nullable=False)
    FundAmount          = db.Column(db.Float, nullable=False)
    FundLastPriceDate   = db.Column(db.String(255), nullable=False)

