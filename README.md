# YouTube Audio Downloader

YouTube Audio Downloader is a simple web application built with Flask that allows users to download audio from YouTube videos by providing a YouTube URL. It extracts the audio from the video and provides it for download in MP3 format.

## Features

- Download audio from YouTube videos by providing a URL.
- Supports multiple audio quality options (depends on the availability of the source video).
- Provides the downloaded audio as an MP3 file for easy offline listening.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/mochiron-desu/yt-music-downloader
   ```

2. Navigate to the project directory:

   ```bash
   cd yt-audio-downloader
   ```

3. Create a virtual environment (recommended) and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and visit `http://127.0.0.1:5000` to access the application.

3. Enter a valid YouTube URL in the provided form and click the "Download" button.

4. The extracted audio in MP3 format will be available for download.

## Screenshots

![Screenshot](https://github.com/mochiron-desu/yt-music-downloader/blob/main/screenshot/img1.png?raw=true)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the [pytube](https://github.com/pytube/pytube) library for handling YouTube video downloads.

## Note

This project is provided as a simple example and may require additional features, improvements, and security measures for production use.

Feel free to contribute to this project or adapt it to your specific requirements.
