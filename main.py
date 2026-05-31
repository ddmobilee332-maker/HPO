# -*- coding: utf-8 -*-
import sys
from paow import main_menu

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\x1b[31m[-] ปิดโปรแกรม\x1b[0m")
        sys.exit()
      
