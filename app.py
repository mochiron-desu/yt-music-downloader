from flask import Flask, request, render_template, send_file
from pytube import YouTube
import os

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def download_audio():
    if request.method == 'POST':
        yt_url = request.form['yt_url']

        if not yt_url:
            return "No URL Provided"

        try:
            yt = YouTube(yt_url)
        except:
            return "URL is not valid"

        # Extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # Download the file
        out_file = video.download(output_path="downloads")


        # Rename and send the file for download
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file,new_file)
        return send_file(new_file, as_attachment=True)
    
        

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
