from flask import Flask,render_template,redirect,request,send_file, url_for
from waitress import serve
from DB.SignIn import signin
from DB.logIn import login
from bson import ObjectId
from DB.upload.upload_PPTS import fs,db # this is your GridFS instance
import io


app=Flask("__main__")
@app.route('/signin',methods=["POST","GET"]) # to update
def Signin():
    if request.method=="POST":
        
        user_name=request.form.get('name')
        user_password=request.form.get('password')
        email=request.form.get('email')

        try:
            signin(user_name,user_password,email)
            print(f"username:{user_name}, pass:{user_password}, email:{email}")
        except Exception as e:  
            return render_template('/signin.html',error=f"Error while signin: {e}")
            
        else:
            return redirect('http://127.0.0.1:2000/login')
            # return redirect(url_for('Login'))
            # return redirect('http://127.0.0.1:2000/')
            # return redirect('templates/index.html')
          
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
            # return render_template('login.html')
            return redirect('http://127.0.0.1:2000/templates/index.html')
            # return redirect('templates/index.html')
        
    else:
        return render_template('login.html')


# @app.route('/')
# def drop_down():
#     cursor = db.fs.find({"metadata.category": "placement"}).sort("metadata.batch", 1)
#     files = []
#     for file_doc in cursor:
#         files.append({
#             "id": str(file_doc["_id"]),
#             "batch": file_doc["metadata"].get("batch", "Unknown"),
#             "filename": file_doc["filename"]
#         })
#     return files

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/list')
def list_pdfs():
    files = fs.find()
    return render_template("list.html", files=files)

# View PDF in browser
@app.route("/view/<file_id>")
def view_pdf(file_id):
    file = fs.get(ObjectId(file_id))
    return send_file(io.BytesIO(file.read()),
                    mimetype="application/pdf",
                    download_name=file.filename)
    
# Download PDF
@app.route("/download/<file_id>")
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