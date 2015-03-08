from psbackend import db

class PSModel:
    """ Inherit this class in the models to prevent code duplication """
    def save(self):
        db.session.add(self)
        db.session.commit()
