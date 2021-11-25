from flask import *
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo_client=PyMongo(app,uri="mongodb+srv://manoj:manoj@cluster0.gnr87.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongo_client.db

@app.route('/login',methods = ['POST','GET'])
def login():
    if(request.method == 'POST'):
        if(request.form):
            email = request.form['userName']
            password = request.form['password'] 
            if(len(email)>0 and len(password)>0):
                db.flask.insert_one(dict(request.form))
                return redirect(url_for('landing'))
            else:
                return ("please fill details")    
        else:
            return redirect(url_for('indexsignup'))
    else:
        return render_template('login.html') 


@app.route('/signup',methods = ['POST','GET'])
def signup():
    if(request.method == 'POST'):
        if(request.form):
            db.flask.insert_one(dict(request.form))
            return redirect(url_for('success'))
        else:
            return redirect(url_for('indexsignup'))
    else:
        return render_template('sign_up.html') 

@app.route('/success')
def success():
   return 'logged in successfully'

@app.route('/signup')
def indexsignup():
    return render_template('sign_up.html')

@app.route('/dashboard')
def landing():
    return render_template('dash_board.html')

@app.route('/forgotpassword')
def forgotpassword():
    return render_template('forgot_password.html')

if __name__ == "__main__" :
    app.run(debug=True)