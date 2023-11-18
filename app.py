from flask import Flask, request, render_template, send_file
from pytube import YouTube, Playlist
import os
import re
import shutil

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def download_audio():
    if request.method == 'POST':
        isPlaylist = False
        yt_url = request.form['yt_url']

        if not yt_url:
            return "No URL Provided"
        
        if "playlist?list" in yt_url:
            isPlaylist = True

        try:
            if isPlaylist:
                yt = Playlist(yt_url)
            else:
                yt = YouTube(yt_url)
        except:
            return "URL is not valid"
        
        download_path = "downloads"

        if isPlaylist:
            yt._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            print(len(yt.video_urls))

            for url in yt.video_urls:
                print(url)

            downloaded_files = []

            for video in yt.videos:
                audioStream = video.streams.filter(only_audio=True).first()
                title = re.sub(r'[\/:*?"<>|]', '', video.title)
                outfile = audioStream.download(output_path = download_path)
                new_file = os.path.join(download_path, f"{title}.wav")
                os.rename(outfile, new_file)
                downloaded_files.append(new_file)
            print("Downloaded")
            
            if isinstance(downloaded_files, list):
                print(f"Starting to Archive... {os.path.join(download_path, 'playlist')}")
                shutil.make_archive(os.path.join("temp", 'playlist'), 'zip', download_path)
                print("Finished zipping...")
                os.rename("temp/playlist.zip",os.path.join(download_path, 'playlist.zip'))
                zip_filename = 'playlist.zip'
                zip_filepath = os.path.join(download_path, zip_filename)
                print(f"zipfile name: {zip_filepath}")
                return send_file(zip_filepath, as_attachment=True)
            else:
                return downloaded_files
        else:
            # Extract only audio
            video = yt.streams.filter(only_audio=True).first()

            # Download the file
            out_file = video.download(output_path=download_path)


            # Rename and send the file for download
            base, ext = os.path.splitext(out_file)
            new_file = f"{base}.wav"
            os.rename(out_file,new_file)
            
            return send_file(new_file, as_attachment=True, mimetype="audio/wav")

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
