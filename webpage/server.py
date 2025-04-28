from flask import Flask, request, render_template
from pytube import YouTube
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    url = request.form.get('url')
    if not url:
        return "Error: 'url'", 400

    try:
        ydl_opts = {'format': 'best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info['url']  # ডাউনলোড লিঙ্ক
            video_title = info.get('title', 'Unknown Title')  # ভিডিওর নাম
    except Exception as e:
        print(f"Error: {e}")
        return f"Error processing YouTube URL: {e}", 400

    return render_template('index.html', video_url=video_url, video_title=video_title)

if __name__ == '__main__':
    app.run(debug=True)