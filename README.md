pip install yt-dlp
python download_youtube.py
pip install tk

যদি python কমান্ড কাজ না করে, তাহলে python3 দিয়ে চালাও:


python3 youtube_downloader_gui.py

yt-dlp এর সর্বশেষ সংস্করণ ব্যবহার করার জন্য নিয়মিত আপডেট করুন:​


yt-dlp -U


আপনার সিস্টেমে FFmpeg ইনস্টল করুন। নিচে Windows-এ FFmpeg ইনস্টল করার ধাপ দেওয়া হলো:

পাথ সেট করুন:

Start Menu-তে Environment Variables লিখে Edit the system environment variables অপশনটি খুলুন।
System Properties উইন্ডোতে Environment Variables বাটনে ক্লিক করুন।
System variables সেকশনে Path নির্বাচন করুন এবং Edit-এ ক্লিক করুন।
New বাটনে ক্লিক করে FFmpeg-এর bin ফোল্ডারের পাথ যোগ করুন (যেমন: C:\ffmpeg\bin )।
সবকিছু OK করে সেভ করুন।

ffmpeg -version

📋 ছোট্ট কিছু টিপস:
১. তুমি ffmpeg_location এ bin ফোল্ডারের পাথ দিলে ঠিক আছে,
তবে আসলে ffmpeg.exe ফাইলের ফোল্ডার দেওয়া উচিত:

মানে ➔

python
'ffmpeg_location': r'C:\ffmpeg\bin\ffmpeg.exe',
এটা দিলে 100% নিশ্চিত হয়ে যাবে yt-dlp ঠিকমতো FFmpeg পাবে।



