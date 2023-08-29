from bson import ObjectId

from flask import render_template
from conn import categorys,products
from app import app

@app.route('/product/<p_id>')
def moreInfo(p_id):
    p_fund = products.find_one({'_id': ObjectId(p_id)})
    if p_fund is None:
        return render_template('error.html')
    else:
        cat_fund = categorys.find_one({'_id':ObjectId(p_fund['cat_id'])})
        return render_template('productInfo.html', p_fund=p_fund,cat_fund=cat_fund)