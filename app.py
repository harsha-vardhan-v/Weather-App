from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
import requests
app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    c_name=request.form['cityname']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+c_name+'&appid=385e11117c5d7da81b09101750eb430f')
    json_object=r.json()
    temp_k=float(json_object['main']['temp'])
    temp_k=temp_k-273.0
    #return json_object
    name=json_object['name']
    cty=json_object['sys']['country']
    return render_template('temperature.html',temp=round(temp_k),city=name,cnty=cty)

@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
