import os
from flask import Flask, render_template, request, redirect, url_for
import cv2

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "./uploads/"
os.makedirs(app.config["IMAGE_UPLOADS"], exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image_path = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)
            image.save(image_path)

            # Process the image and identify contours (call your function here)
            # Example: contours_info = identify_contours([image_path], root_path)

            return render_template("upload_image.html", uploaded_image=image_path)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
