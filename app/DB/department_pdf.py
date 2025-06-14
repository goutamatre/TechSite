# from flask import Blueprint,Flask,send_file, render_template
from bson import ObjectId
import io
from upload.upload_PPTS import fs # this is your GridFS instance
# from waitress import serve 

# routes_bp = Blueprint("routes", __name__)


# List all uploaded PDFs
def list_pdfs():
    files = fs.find()
    return render_template("pdf_list.html", files=files)

# View PDF in browser
# @routes_bp.route("/view/<file_id>")
def view_pdf(file_id):
    file = fs.get(ObjectId(file_id))
    return send_file(io.BytesIO(file.read()),
                    mimetype="application/pdf",
                    download_name=file.filename)
    
# Download PDF
@routes_bp.route("/download/<file_id>")
def download_pdf(file_id):
    try:
        file = fs.get(ObjectId(file_id))
        return send_file(io.BytesIO(file.read()),
                         mimetype="application/pdf",
                         as_attachment=True,
                         download_name=file.filename)
    except:
        return "PDF not found", 404
    
    
# app = Flask(__name__)
# app.register_blueprint(routes_bp)
