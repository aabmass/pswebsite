from flask import Response, request

from psbackend import app
from psbackend.templateutil import render

from psbackend.models.product import Product

from psbackend.forms.product import CreateProductForm

@app.route('/product/<int:id>')
def product(id):
    prod = Product.query.get(id)
    return render("product.html", product=prod, pageTitle=prod.name) 

@app.route('/product/create', methods=['POST'])
def createProduct():
    """ View to create product; requires admin priveleges! """
    form = CreateProductForm(request.form)

    if current_user.notAdmin():
        return Response(status=403)
    elif form.validate():
        name = form.name.data
        desc = form.desc.data
        isEnabled = form.isEnabled.data
    
        product = Product(name, desc, isEnabled=isEnabled)
        user.save()
        login_user(user)
        return Response(status=200, response=product.id)
    else:
        return Response(status=500)
