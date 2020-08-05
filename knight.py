import random
import time
import sys, pyautogui

try:
	while True:
		randint = random.uniform(0.416,0.703)
		print(randint)
		time.sleep(randint)
		pyautogui.click()

except KeyboardInterrupt:
	pass
