from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
      
       a = request.form.get("amortality")
       b = request.form.get("bmi")
       c = request.form.get("polio")
       d = request.form.get("diph")
       e = request.form.get("hiv")
       f = request.form.get("gdp")
       g = request.form.get("t1")
       h = request.form.get("t2")
       i = request.form.get("income comp")
       j = request.form.get("schooling")
       
       list_ = [a,b,c,d,e,f,g,h,i,j]

       return "The final output is " + list_
    return render_template("hv final pred.html")
 
if __name__=='__main__':
   app.run()

from flask import Flask, render_template, request
import numpy as np
from joblib import load
from sklearn.linear_model import LinearRegression

app= Flask(__name__)

@app.route("/predict",methods = ["GET","POST"])
def predictModel():
    request_type_str=request.method
    if request_type_str == "GET":
        return render_template("index.html", href = "static/base_pic.svg")
    else:
        text = request.form["text"]
        path = "static/base_pic.svg"
        return render_template("index.html", href = path)

@app.route("/",methods = ["GET","POST"])
def mainPage():
    # return render_template("index.html",href = "static/base_pic.svg")
    return render_template("hv main.html")

@app.route("/predict",methods = ["GET","POST"])
def hv2022():
    return render_template("hv2022.html")


if __name__=="__main__":
    app.run(debug=True)

