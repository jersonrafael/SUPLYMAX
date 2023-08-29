from flask import render_template
from conn import categorys,products
from app import app

@app.route('/', methods=['GET'])
def home():
    find_cat = categorys.find()
    alls_products = products.find()
    return render_template('home.html', alls_products=alls_products,p_categorys=find_cat)

