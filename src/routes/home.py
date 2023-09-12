from flask import render_template
from conn import categorys,products
from app import app

from priceBs import obtenerUsd


priceVes = obtenerUsd()
# princeVes = priceVes[0:7].replace(',', '.')

def actualizar_precio_dolar_en_todos_los_productos(nuevo_precio_dolar):
    # Define la actualización que deseas realizar para todos los documentos
    price = products.find()
    for x in price:
        convert = priceVes.replace(',', '.')
        y = x['p_price'].replace(',','.')
        precio = float(y) * float(convert)
        precio = str(precio)
        products.update_one({'_id': x['_id']}, {"$set": {'priceVes': precio[0:7]}})


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route('/info')
def info():
    actualizar_precio_dolar_en_todos_los_productos(priceVes)
    return render_template('info.html')

@app.route('/home', methods=['GET'])
def home():
    find_cat = categorys.find()
    alls_products = products.find()
    products_quantity = products.count_documents({})
    return render_template('home.html', alls_products=alls_products,p_categorys=find_cat,products_quantity=products_quantity)