from flask import Flask, render_template, url_for, redirect, request,jsonify
import os
app = Flask(__name__)


@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/upload",methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        file.save(os.path.join("uploads",file.filename))
        #return redirect(url_for('home'))
        return render_template('upload.html',message="File has been successfully uploaded")
    return render_template('upload.html',message="")

if __name__ == '__main__':
    app.run(debug=True)





