import time
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

def TestThread():

	print("in testThread function...")
	# wait for 5 seconds
	time.sleep(1) 

	# return some message after waiting
	test = "This is a test."

	return test

