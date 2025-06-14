from flask import Flask,render_template,redirect,request
from waitress import serve
from DB.SignIn import signin
from DB.logIn import login
from DB.department_pdf import views,drop_down

app=Flask("__main__")

@app.route('/signin',methods=["POST","GET"]) # to update
def Signin():
    if request.method=="POST":
        
        user_name=request.form.get('name')
        user_password=request.form.get('password')
        data=signin(user_name,user_password)
        
        if data==False:
            return render_template('signin.html',error="error while signing in")
        else:
            return redirect('/')
    
    else:
        return render_template('signin.html')
    

@app.route('/login',methods=["POST","GET"])
def Login():
    if request.method=="POST":
        user_name=request.form.get('name')
        user_password=request.form.get('password')
        data=login(user_name, user_password)
        
        if data==False:
            return render_template('login.html', error="Credintials not match")
        else:
            return redirect('/')
        
    else:
        return render_template('login.html')

@app.route('/')
def placement():
    return drop_down()

@app.route('/view/<file_id>')
def view(file_id):
    return views(file_id)
