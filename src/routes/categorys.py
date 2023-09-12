from flask import render_template
from conn import categorys,products
from bson import ObjectId
from app import app

@app.route('/category/<category_id>')
def catSearch(category_id):
    products_quantity = products.count_documents({"cat_id":category_id})
    find_cat = categorys.find_one({"_id":ObjectId(category_id)})
    all_products_cat = products.find({"cat_id": category_id})
    return render_template('categorys.html', name=find_cat,products_find=all_products_cat,products_quantity=products_quantity)

@app.route('/allcategorys')
def allcategorys():
    find_cat = categorys.find()
    return render_template('allcategorys.html', categorys= find_cat)