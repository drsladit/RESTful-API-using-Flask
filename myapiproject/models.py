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
    PremiumAmount       = db.Column(db.Float(precision=2), nullable=False)
    CoverageStartDate   = db.Column(db.DateTime, nullable=False)
    CoverageEndDate     = db.Column(db.DateTime, nullable=False)
    FundIndicator       = db.Column(db.Boolean, nullable=False)

    # Relationship with back_populates
    Plans          = db.relationship("PlansTable", back_populates="Policys", lazy="dynamic")
    Funds          = db.relationship("FundsTable", back_populates="Policys", lazy="dynamic")

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
    SumInsured = db.Column(db.Float(precision=2), nullable=False)

    # Relationship with back_populates
    Policys          = db.relationship("PolicysTable", back_populates="Plans")


class FundsTable(db.Model):
    __tablename__ = "FundsTable"

    FundId              = db.Column(db.Integer, primary_key=True)
    PolicyId            = db.Column(db.Integer, db.ForeignKey('PolicysTable.PolicyId'), nullable=False)
    FundName            = db.Column(db.String(255), nullable=False)
    FundAmount          = db.Column(db.Float(precision=2), nullable=False)
    FundLastPriceDate   = db.Column(db.DateTime, nullable=False)

    # Relationship with back_populates
    Policys          = db.relationship("PolicysTable", back_populates="Funds")


class UserTable(db.Model):
    __tablename__ = "UserTable"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


