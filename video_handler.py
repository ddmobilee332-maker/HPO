# -*- coding: utf-8 -*-
import yt_dlp

def get_video_details(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'format': 'bestaudio/best',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                'title': info.get('title', 'ไม่ทราบชื่อ'),
                'author': info.get('uploader', 'ไม่ทราบช่อง'),
                'duration': info.get('duration', 0),
                'views': f"{info.get('view_count', 0):,}",
                'audio_url': info.get('url')
            }
    except Exception:
        return None
      
