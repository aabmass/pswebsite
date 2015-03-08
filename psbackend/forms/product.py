from wtforms import Form, BooleanField, StringField, TextField, validators

class CreateProductForm(Form):
    name = StringField('Product Name', [validators.Required()])
    desc = TextField('Production Description', [validators.Required()])
    isEnabled = BooleanField('Is Enabled', [validators.Optional()])
