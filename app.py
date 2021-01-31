from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
import requests
app = Flask(__name__)

searches = []

@app.route('/temperature', methods=['POST'])
def temperature():
    city_details = {}
    c_name=request.form['cityname']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+c_name+'&appid=385e11117c5d7da81b09101750eb430f')
    json_object=r.json()
    temp_k=float(json_object['main']['temp'])
    city_details['temp']=round(temp_k-273.0)

    #return json_object
    city_details['name']=json_object['name']
    city_details['country']=json_object['sys']['country']

    searches.insert(0, city_details)

    if(len(searches)>7):
        searches.pop(len(searches)-1)

    return render_template('temperature.html',search_list = searches)

@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
