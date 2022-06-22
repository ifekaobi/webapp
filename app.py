from flask import Flask,redirect,url_for,render_template,request
from config import port, host, debug

app=Flask(__name__)

from routes import *

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host=host, port=port,debug=debug)