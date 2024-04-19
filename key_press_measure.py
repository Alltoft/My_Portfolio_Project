import time
import sys
import tty
import termios



# input()
# while True:
#     Time = time.time()
#     tty.setcbreak(sys.stdin.fileno())  # Set the terminal to raw mode
#     sys.stdin.read(1)
#     time.sleep(0.111)
#     current_time = time.time()

#     time_passed = current_time - Time
#     time_str = str(time_passed)

#     print(f"the time passed is {time_str[:5]}")
termios.tcgetattr(sys.stdin)