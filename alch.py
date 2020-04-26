import random
import time
import sys, pyautogui
from progress.bar import ChargingBar

try:
	mod = random.randint(6,14)
	alchs = int(input("How many items to alch?:"))
	bar = ChargingBar('Alching', max = alchs)
	for i in range(alchs):
		randint = 1.1+random.uniform(0,0.8)
		time.sleep(randint)
		pyautogui.click()
		
		if (i % mod) == 0:
			time.sleep(random.uniform(1,2))

		randint = 1.1+random.uniform(0,0.8)
		time.sleep(randint)
		pyautogui.click()
		bar.next()
	bar.finish()
except KeyboardInterrupt:
	pass
