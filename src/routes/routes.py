from app import app
from . import home,categorys,productInfo

#MANEJADOR DE ERRORES
@app.errorhandler(404)
def page_not_found(e):
    return 'La pagina no existe'