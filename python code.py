from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__, template_folder='web')
loaded_model = joblib.load('model.joblib')


@app.route('/', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        #to_predict_list = request.form.to_dict()
        #to_predict_list = list(to_predict_list.values())
        #to_predict_list = list(map(float, to_predict_list))
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
        result = loaded_model.predict(list_)
        return render_template("hv final pred.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)