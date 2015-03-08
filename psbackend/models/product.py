import datetime

from psbackend import db
from psbackend.models.psmodel import PSModel

class Product(db.Model, PSModel):
    # Basic info
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, default='')
    desc = db.Column(db.Text(), nullable=False, default='')

    creationDate = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    # Whether or not this product is enabled for sales
    isEnabled = db.Column(db.Boolean(), nullable=False, default=False)

    def __init__(self, name, desc, isEnabled=False):
        self.name = name
        self.desc = desc
        self.isEnabled = isEnabled

    def __str__(self):
        return self.name
