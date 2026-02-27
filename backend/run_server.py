#!/usr/bin/env python
import sys
import subprocess
import time

# Run Flask app
if __name__ == '__main__':
    subprocess.Popen([sys.executable, 'app.py'], 
                    cwd=r'c:\Users\hp\Desktop\IBM\badawy-timezone-converter\backend')
    time.sleep(2)
    print("Server started on port 5000")
