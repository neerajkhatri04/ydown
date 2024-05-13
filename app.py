from flask import Flask, render_template, request
from extractor import get_video_data
from extra import FAQS
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", faqs=FAQS)

@app.route("/download", methods=["POST"])
def download():
        video_url = request.form["video_url"]
        video_data = get_video_data(video_url)
        title = video_data["title"]
        thumbnail = video_data["thumbnail"]
        formats = video_data["formats"]
        return render_template("download.html",title=title, thumbnail=thumbnail, formats=formats, video_data=video_data)

if __name__ == '__main__':
    app.run(debug=True)