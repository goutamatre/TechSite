from flask import Flask,render_template,redirect,request,send_file
from waitress import serve
from app.DB.SignIn import signin
from app.DB.logIn import login
from bson import ObjectId
from app.DB.upload.upload_PPTS import fs,db # this is your GridFS instance
import io
from flask_cors import CORS

app=Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signin',methods=["POST","GET"]) # to update
def Signin():
    if request.method=="POST":
        
        user_name=request.form.get('name')
        user_password=request.form.get('password')
        email=request.form.get('email')
    
        try:
            signin(user_name,user_password,email)
        except Exception as e:
            return render_template('signin.html',error=f"Error while signin: {e}")
            
        else:
            return redirect('http://127.0.0.1:5500/templates/index.html')
          
        # http://127.0.0.1:5500/templates/index.html
    
    else:
        return render_template('signin.html')
    

@app.route('/login',methods=["POST","GET"])
def Login():
    if request.method=="POST":
        email=request.form.get('email')
        user_password=request.form.get('password')
        
        result= login(email, user_password)
        if result==None:
            return render_template('login.html', error="Error in login")
        
        else:
            return redirect('http://127.0.0.1:5500/templates/index.html')
        
    else:
        return render_template('login.html')

@app.route('https://lncts.onrender.com/list')
def list_pdfs():
    files = fs.find()
    return render_template("list.html", files=files)

# View PDF in browser
@app.route("/app/view/<file_id>")
def view_pdf(file_id):
    file = fs.get(ObjectId(file_id))
    return send_file(io.BytesIO(file.read()),
                    mimetype="application/pdf",
                    download_name=file.filename)
    
# Download PDF
@app.route("/app/download/<file_id>")
def download_pdf(file_id):
    try:
        file = fs.get(ObjectId(file_id))
        return send_file(io.BytesIO(file.read()),
                         mimetype="application/pdf",
                         as_attachment=True,
                         download_name=file.filename)
    except:
        return "PDF not found", 404
    
if __name__=="__main__":
    serve(app,host='0.0.0.0', port=2000)