# -*- coding: utf-8 -*-
import os
import subprocess

def play_audio_stream(url):
    if not url:
        print('\x1b[31m[!] ไม่พบไฟล์เสียงของคลิปนี้\x1b[0m')
        return

    # เช็คว่าเป็นระบบ Termux (Android) หรือไม่
    is_termux = os.path.exists('/data/data/com.termux')

    try:
        if is_termux:
            # ตรวจสอบและใช้ mpv หรือ play-audio ของ termux ในการเปิดสตรีมเสียงทันทีโดยไม่ต้องใช้ pygame
            # ติดตั้งง่ายผ่าน pkg install mpv -y
            subprocess.run(['mpv', '--no-video', url], check=True)
        else:
            # ถ้าเอาไปรันบน Windows (เปิดผ่านเว็บเบราว์เซอร์หรือเครื่องเล่นหลัก)
            os.system(f'start "" "{url}"')
    except Exception as e:
        print(f'\x1b[31m[!] การเล่นเสียงขัดข้อง (กรุณาพิมพ์ pkg install mpv -y ใน Termux): {e}\x1b[0m')
      
