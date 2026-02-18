import os
from flask import Flask, render_template, request, url_for
from model import predict

app = Flask(__name__)

# Ensure static directory for uploads exists
UPLOAD_FOLDER = os.path.join(app.root_path, "static/uploads")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file1" not in request.files:
            return "No file uploaded!"

        file1 = request.files["file1"]

        if file1.filename == "":
            return "No selected file!"

        if file1 and allowed_file(file1.filename):
            filename = file1.filename
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file1.save(filepath)

            # Run prediction
            prediction = predict(filepath)

            # Convert model output to readable text
            result = "No Brain Cancer" if prediction > 0.5 else "Brain Cancer"

            # Corrected Image Path for Rendering
            image_url = url_for("static", filename=f"uploads/{filename}")

            return render_template("index.html", result=result, image_path=image_url)

    return render_template("index.html", result=None, image_path=None)

if __name__ == "__main__":
    app.run(debug=True)
