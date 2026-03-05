from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route("/")
def home():
    return "Toolkit YouTube Video Downloader Running"

@app.route("/download")
def download():

    url = request.args.get("url")

    if not url:
        return {"error":"No URL provided"}

    ydl_opts = {
        'format': 'best',
        'outtmpl': DOWNLOAD_FOLDER + '/video.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run()
