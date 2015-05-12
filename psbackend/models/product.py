from psbackend import db

import datetime

sizes = {
    'small': '20x20',
    'medium': '25x20',
    'large': '30x20'
}

class Product(db.Model):
    # Product number, primary key, int
    productId = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)

    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False, default='poster')
    description = db.Column(db.String(255), nullable=True)
    size = db.Column(db.String(255), nullable=True, default=sizes['small'])

    isEnabled = db.Column(db.Boolean(), nullable=False, default=True)
    createdOn = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    def __init__(self, name, category, description, size=sizes['small']):
        self.name = name
        self.category = category
        self.description = description
        self.size = size

    def save(self):
        db.session.add(self)
        db.session.commit()
