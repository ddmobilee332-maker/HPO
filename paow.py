# -*- coding: utf-8 -*-
import os
from video_handler import get_video_details
from audio_handler import play_audio_stream

def show_pao_logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    # โลโก้คำว่า "เปา" ภาษาไทย ตัวใหญ่ ๆ สลับสี ANSI ดุดัน
    print("\x1b[91m      ██████╗  █████╗  ██████╗ \x1b[0m")
    print("\x1b[93m      ██╔══██╗██╔══██╗██╔═══██╗\x1b[0m")
    print("\x1b[92m      ██████╔╝███████║██║   ██║\x1b[0m")
    print("\x1b[96m      ██╔═══╝ ██╔══██║██║   ██║\x1b[0m")
    print("\x1b[95m      ██║     ██║  ██║╚██████╔╝\x1b[0m")
    print("\x1b[94m      ╚═╝     ╚═╝  ╚═╝ ╚═════╝ \x1b[0m")
    print("\n\x1b[97m==============================================\x1b[0m")
    print("\x1b[92m           ยินดีต้อนรับสู่ ระบบ เปา เทพที่สุด          \x1b[0m")
    print("\x1b[97m==============================================\x1b[0m\n")

def ask_for_audio(audio_url):
    while True:
        choice = input("\x1b[35m[?] คุณต้องการจะเปิดเสียงนี้ไหม? (y/n): \x1b[0m").strip().lower()
        if choice == 'y':
            print('\x1b[32m[+] กำลังเปิดเสียงในเครื่องให้ทันที...\x1b[0m')
            play_audio_stream(audio_url)
            input("\n\x1b[32m[✓] เล่นเสียงเสร็จสิ้น! กด Enter เพื่อกลับหน้าหลัก...\x1b[0m")
            main_menu()
            break
        elif choice == 'n':
            print('\x1b[31m[-] ยกเลิกการเปิดเสียง\x1b[0m')
            input("\nกด Enter เพื่อกลับหน้าหลัก...")
            main_menu()
            break
        else:
            print('\x1b[33m[!] ตอบแค่ y หรือ n เท่านั้นนะพี่\x1b[0m')

def main_menu():
    show_pao_logo()
    video_link = input("\x1b[36m[เปา] วางลิงก์คลิปวิดีโอที่นี่: \x1b[0m").strip()
    
    if not video_link:
        print('\x1b[31m[!] กรุณาใส่ลิงก์ให้ถูกต้อง\x1b[0m')
        input("\nกด Enter เพื่อลองใหม่...")
        main_menu()
        return

    print('\n\x1b[33m[*] กำลังดึงรายละเอียดจากคลิป สักครู่พี่...\x1b[0m')
    data = get_video_details(video_link)

    if not data:
        print('\x1b[31m[!] ไม่สามารถดึงข้อมูลคลิปนี้ได้ หรือลิงก์ไม่ถูกต้อง\x1b[0m')
        input("\nกด Enter เพื่อกลับหน้าหลัก...")
        main_menu()
        return

    print(f"\n\x1b[92m=== รายละเอียดคลิป ===\x1b[0m")
    print(f"📌 ชื่อคลิป: {data['title']}")
    print(f"👤 ช่อง: {data['author']}")
    print(f"⏱️ ความยาว: {data['duration']} วินาที")
    print(f"👁️ ยอดวิว: {data['views']} ครั้ง")
    print(f"======================\n")

    ask_for_audio(data['audio_url'])
  
