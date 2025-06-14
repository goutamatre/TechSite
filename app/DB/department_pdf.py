from bson import ObjectId
import io
from DB.upload.upload_PPTS import fs,db # this is your GridFS instance


def drop_down():
    cursor = db.fs.files.find({"metadata.category": "placement"}).sort("metadata.batch", 1)
    files = []
    for file_doc in cursor:
        files.append({
            "id": str(file_doc["_id"]),
            "batch": file_doc["metadata"].get("batch", "Unknown"),
            "filename": file_doc["filename"]
        })
# List all uploaded PDFs
def views(file_id):
    try:
        grid_out = fs.get(ObjectId(file_id))
        return drop_down(grid_out.read(), mimetype='application/pdf')
    except Exception as e:
        return f"Error: {e}", 404
