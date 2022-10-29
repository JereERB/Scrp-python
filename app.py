from distutils.log import debug
from itertools import product
from flask import Flask, jsonify
import flask
import json
#Objeto que inicializa mi servidor
app = Flask(__name__)

from scrap import Scrapy  

@app.route('/ping')
def ping():
    return jsonify({
        "message": "Ping 20ms"
    })

@app.route('/scrap')
def getProducts():
    sc  = Scrapy()
    sc.first_window()
    data =  sc.secondo_window()
    return jsonify({"Productos":data}) 

if __name__ == '__main__':
    app.run(debug=True,port=4000)




