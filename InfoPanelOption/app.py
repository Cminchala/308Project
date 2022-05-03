
from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from requests import get
import requests
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ipQuery.db'
db = SQLAlchemy(app)



ip = ""



@app.route('/', methods = ["GET","POST"]) ## NOT DONE JUST A START THO :)
def ipInfo():
    urls = "http://ipwho.is/"
    if request.method == "POST":
        ipe = request.form.get("ip")
        ip = ipe
        urls += ip
        resp = requests.get(urls)
        return resp.text
    return render_template("ipInfo.html")

@app.route('/map') ### URL GET FUNCTION ADD IN THE THE HTML {{}}
def mapInfo():
    return ip
    


if __name__ == "__main__":
    app.run(debug =True)

