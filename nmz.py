import random
import time
import sys, pyautogui

try:
	while True:
		randint = random.uniform(40,58)
		print(randint)
		time.sleep(randint)
		pyautogui.click()
		
		time.sleep(random.uniform(0.3,0.8))
		pyautogui.click()

except KeyboardInterrupt:
	pass
