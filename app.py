from flask import Flask, render_template, url_for, redirect, request,jsonify
import os
import pandas as pd
import pickle5 as pickle

app = Flask(__name__)

#load model
model = pickle.load(open("model.pkl","rb"))


@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/upload",methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        file.save(os.path.join("uploads",file.filename))
        #file.save(os.path.join( os.path.dirname(__file__),app.config["UPLOADS"],file.filename))
        #return redirect(url_for('home'))
        return render_template('upload.html',message="File has been successfully uploaded")
    return render_template('upload.html',message="")

@app.route("/test",methods=['POST'])
def test():
    data = request.get_json() #return a dictionary
    df = pd.DataFrame([data]) #convert to dataframe
    print (df.shape)
    #name = data['name']
    #location = data['location']
    prediction = model.predict(df)
    #print(type(prediction))

    return jsonify({'result':'Success','prediction':prediction[0]})
if __name__ == '__main__':
    app.run(debug=True)





