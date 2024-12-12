import os
import random
import time

chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[]{};:'\",.<>?/\\|"
width = os.get_terminal_size().columns

while True:
    print("".join(random.choice(chars) for _ in range(width)))
    time.sleep(0.05)
