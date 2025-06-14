from flask import Flask, request, jsonify,render_template
from pymongo import MongoClient
from waitress import serve
import gridfs

app = Flask(__name__)

# MongoDB connection
with open("my_credentials", "r") as file:
    username = file.readline().strip()
    password=file.readline().strip()

client=MongoClient( f"mongodb+srv://{username}:{password}@cluster0.xnjfjzj.mongodb.net/")

db = client["pdf_database"]
fs = gridfs.GridFS(db)

@app.route("/upload", methods=["POST","GET"])
def upload_pdf():
    if request.method=="GET":
        return render_template("upload.html")
    file = request.files.get("pdf")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Save PDF in GridFS
    file_id = fs.put(file, filename=file.filename)
    
    return jsonify({"message": "PDF uploaded successfully", "file_id": str(file_id)})

if __name__ == "__main__":
    serve(app,host='0.0.0.0', port=5000)