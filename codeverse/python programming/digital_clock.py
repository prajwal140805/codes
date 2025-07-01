import time
import sys

while True:
    current_time = time.strftime("%H:%M:%S", time.localtime())
    sys.stdout.write("\r" + current_time)
    sys.stdout.flush()
    time.sleep(1)

