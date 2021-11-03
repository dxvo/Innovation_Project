from flask import Flask, render_template, url_for, redirect, request,jsonify
import pandas as pd
import pickle5 as pickle
from forms import *
from collections import defaultdict

app = Flask(__name__)

#load model
model = pickle.load(open("model.pkl","rb"))
app.config['SECRET_KEY'] = 'a26ade032e7040309ba635818774a38b'


@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/makePrediction", methods=['GET','POST'])
def makePrediction():
    form = Machinedata()
    dict = defaultdict(int) #default dictionary

    if form.validate_on_submit():        
        dict["machineID"] = form.machineID.data
        dict["volt"] = form.volt.data
        dict["rotate"] = form.rotate.data
        dict["vibration"] = form.vibration.data
        dict["pressure"] = form.pressure.data
        dict["model"] = form.model.data
        dict["age"] = form.age.data
        dict["comp"] = form.comp.data
        dict["time since last service (hrs)"] = form.lastService.data
        dict["time since last failure (hrs)"] = form.lastFailure.data
        
        df = pd.DataFrame([dict]) #convert dictionary to dataframe
        prediction = model.predict(df)
        #print(f'Machine needs maintainance in',prediction[0]/24,'day(s)')
        return render_template('displayResult.html', message = "Machine needs maintainance in {} day(s).".format(round(prediction[0]/24),2))
    return render_template('getMachineData.html',form=form)

@app.route("/API",methods=['POST'])
def API():
    data = request.get_json() #return a dictionary
    df = pd.DataFrame([data]) #convert to dataframe
    prediction = model.predict(df)
    return jsonify({'Status':'Success','Prediction':prediction[0]}),201

if __name__ == '__main__':
    app.run(debug=True)





