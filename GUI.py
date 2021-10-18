from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import threading
import time
from Test_File import TestThread
import concurrent.futures
# TESTING:
import sys
# sys.path.append('./pythonCamera')
sys.path.insert(1, '../pythonCamera')
from start import test_function
#sys.path.insert(1, '../pythonSimulator')
#from example import test_put_obstacle
import numpy as np




# Window should look like:
#    column 0        column 1
# -------------------------------
# |             |               |
# |    first    |    second     |
# |   section   |   section     |   row 0
# |             |               |
# -------------------------------
# |                             |
# |       third section         |   row 1
# |                             |
# -------------------------------


class GUI_Functions():

	def __init__(self, root):

		root.geometry("1100x900")

		# elements for the first section of the window grid
		self.section_1 = Label(root, text="This is the first section of the window.\n [This is where the camera image will be loaded]", bg="MediumPurple1")
		self.section_1.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)

		# elements for the second section of the window grid
		self.section_2 = Label(root, text="This is the second section of the window.\n [This is where the simulation will be visible]", bg="SteelBlue2").grid(column=2, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
		self.add_object_btn = Button(root, text="Add object", command=self.add_objects_clicked).grid(column=2, row=1, sticky=S, pady=15)

		self.remove_obejct_btn = Button(root, text="Remove object", command=self.remove_objects_clicked).grid(column=3, row=1, sticky=S, pady=15)

		# make self.placeholder here be the loaded simulatin.py file
		self.placeholder = Label(root, text="This is a placeholder for where the simulation will be displayed.", bg="White", width=15, height=30).grid(column=2, row=0, columnspan=2, rowspan=1, sticky=N+E+S+W, padx=20, pady=20)

		# elements for the third section of the window grid
		self.section_3 = Label(root, text="This is the third section of the window.\n ", bg="Orchid2").grid(columnspan=4, row=2, sticky=N+E+S+W)

		# configuring columns and rows
		Grid.columnconfigure(root, 0, weight=1)
		Grid.columnconfigure(root, 1, weight=1)
		Grid.columnconfigure(root, 2, weight=1)
		Grid.columnconfigure(root, 3, weight=1)
		Grid.rowconfigure(root, 0, weight=0)
		Grid.rowconfigure(root, 1, weight=0)
		Grid.rowconfigure(root, 2, weight=3)

	# uses a thread to load camera image code separate from the GUI window
	def load_camera_image(self):
		pass

	# displays the simulation 
	def show_simulation(self):
		# TODO: figure out how to embed the arcade window in this GUI window
		pass

	# handles the event where the 'add objects' to simulation button is clicked
	def add_objects_clicked(self):
		self.add_window = Toplevel(root)
		self.add_window.geometry("400x400")
		self.add_window.title("Add Object")

		lbl = Label(self.add_window, text="Enter the values for an object to add.").grid(column=0, row=0)
		e_lbl = Label(self.add_window, text="Enter a name for the object: ").grid(column=0, row=1)
		self.e = Text(self.add_window, height=1, width=10)
		self.e.grid(column=1, row=1)
		e1_lbl = Label(self.add_window, text="Enter an x-value: ").grid(column=0, row=2)
		self.e2 = Text(self.add_window, height=1, width=10)
		self.e2.grid(column=1, row=2)
		self.e3_lbl = Label(self.add_window, text="Enter a y-value: ").grid(column=0, row=3)
		self.e3 = Text(self.add_window, height=1, width=10)
		self.e3.grid(column=1, row=3)
		e4_lbl = Label(self.add_window, text="Enter an angle value: ").grid(column=0, row=4)
		self.e4 = Text(self.add_window, height=1, width=10)
		self.e4.grid(column=1, row=4)
		e5_lbl = Label(self.add_window, text="Enter a width value: ").grid(column=0, row=5)
		self.e5 = Text(self.add_window, height=1, width=10)
		self.e5.grid(column=1, row=5)
		e6_lbl = Label(self.add_window, text="Enter a height value: ").grid(column=0, row=6)
		self.e6 = Text(self.add_window, height=1, width=10)
		self.e6.grid(column=1, row=6)
		add_btn = Button(self.add_window, text="Add", command=self.add_btn_clicked).grid(column=0, row=7)
		cancel_btn = Button(self.add_window, text="Cancel", command=lambda: self.cancel_btn_click(self.add_window)).grid(column=2, row=7)

	# handles the event where the 'remove objects' from simulation button is clicked
	def remove_objects_clicked(self):
		self.remove_window = Toplevel(root)
		self.remove_window.geometry("400x400")
		self.remove_window.title("Remove Object")
		lbl = Label(self.remove_window, text="Enter the name of the object to remove.").pack()
		e = Entry(self.remove_window, width=20).pack()
		remove_btn = Button(self.remove_window, text="Remove", command=self.remove_btn_clicked).pack()
		cance_btn = Button(self.remove_window, text="Cancel", command=lambda: self.cancel_btn_click(self.remove_window)).pack()

	def cancel_btn_click(self, window_to_close):
		print("** button clicked to cancel **")
		window_to_close.destroy()

	# MIGHT NEED TO RUN LAB FIRST VFOR THIS TO WORK??
	def add_btn_clicked(self):
		# do stuff for when "add" object button is clicked
		print("** Add button clicked **")
		print("Test entries: ", self.e.get("1.0", 'end-1c'), self.e2.get("1.0", 'end-1c'), self.e3.get("1.0", 'end-1c'), self.e4.get("1.0", 'end-1c'), self.e5.get("1.0", 'end-1c'), self.e6.get("1.0", 'end-1c'))


		#test_put_obstacle(obstacle_name, x, y, angle, width, height)
		#test_put_obstacle("ObstacleTest", 0.5, 0.5, 0.0, 0.5, 2.4)
		print("Check if obstacle was placed correctly...")



	def remove_btn_clicked(self):
		# do stuff for when "remove" object button is clicked
		print("** Remove button clicked **")

	# testing how to add ndarray as image to the GUI window
	# def test_ndarray_image(self, image_array):

	# 	img_2, img_h = 200, 200
	# 	data = np.zeros((img_h, img_2, 3), dtype=np.uint8)
	# 	data[100, 100] = [255, 0, 0]
		
	# 	self.img = Image.fromarray(data, image_array)
	# 	self.section_1.config(image=self.img)
	# 	self.section_1.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
	# 	self.section_1.update()

		# self.img_1 = ImageTk.PhotoImage(image_array).resize((400, 200))

		# self.section_1.config(image=self.img_1)
		# self.section_1.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
		# self.section_1.update()



	# function to test adding an image to the GUI window
	def test_add_image(self):

		self.image_1 = Image.open("./image_2.jpeg").resize((400, 200))
		self.img_1 = ImageTk.PhotoImage(self.image_1)

		self.section_1.config(image=self.img_1)
		self.section_1.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
		self.section_1.update()

	# function to test updates to GUI window
	def test_updates(self, value_of_update):

		print("---> Is in test_updates function")

		#self.section_1 = Label(root, text=value_of_update)
		self.section_1.config(text=value_of_update)
		self.section_1.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)

		self.section_1.update()

		self.test_add_image()


	# function to update GUI window by displaying the 'frame' object found from (D:Workspace/pythonCamera/start.py)
	def test_display_startPY(self):
		# ../pythonCamera/start.py
		print("---> testing start.py")
		returned_val = test_function()

		print("type of return value: ", type(returned_val)) # --> type is: numpy.ndarray
		# print("try to open array...", returned_val[0]) # --> trying to get into the array to see what it does

		array = np.ones((40, 40))*150
		img = ImageTk.PhotoImage(image=Image.fromarray(array))
		# canvas = Canvas(width=3000, height=300)
		# canvas.pack()
		# canvas.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
		
		#to_display = canvas.create_image(20,20, anchor="nw", image=img)
		# self.section_1.update()
		self.section_1.config(image=img)
		self.section_1.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
		self.section_1.update()

		# return returned_val

		# print("Now displaying returned image...")
		# self.image_1 = Image.open(returned_val).resize((400, 200))
		# self.img_1 = ImageTk.PhotoImage(self.image_1)

		# self.section_1.config(image=self.img_1)
		# self.section_1.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
		# self.section_1.update()

		# self.img_1 = ImageTk.PhotoImage(to_display)

		# self.section_1.config(image=self.img_1)
		# self.section_1.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
		# self.section_1.update()


def test_thread():
	print("---> Before executor...")
	with concurrent.futures.ThreadPoolExecutor() as executor:
		future = executor.submit(TestThread)
		return_value = future.result()

	print("---> before test_updates...")
	# try to update the GUI window with new text value
	gui_fun.test_updates(return_value)
	print("---> after test_updates...")

	print("------> testing start.py")
	image_to_display = gui_fun.test_display_startPY()

	# print("---> Now trying to display the returned value for the camera image...")
	# gui_fun.test_ndarray_image(image_to_display)



def start_thread():
	print("starting thread...")
	test_thread = threading.Thread(target = test_thread())
	test_thread.start()

if __name__ == '__main__':
	print("running... ")
	root = Tk()
	root.title('Lab GUI Window')
	gui_fun = GUI_Functions(root)
	# root.mainloop() 

	# added recently -- has not been tested yet!
	#sys.path.insert(0, 'D:Workspace/pythonCamera/start.py')


	# NOTE:
	# if mainloop() is called first, then it runs the tkinter window and not the thread below
	# if the thread below is called before mainloop(), then it runs the code in the thread first, then opens the tkinter window with the updates from the code second

	# this works to run the other code and update the GUI window.. but doesn't run at the same time as the tkinter window - loads this first, then the window
	# print("starting  thread...")
	# test_thread = threading.Thread(target = test_thread())
	# test_thread.start() # --> dont do this here, do this thread inside of a callback function

	# root.mainloop()

	firstRun = True

	while True:
		root.update_idletasks()
		root.update()

		if firstRun:
			print("is visible.")
			print("starting  thread...")
			test_thread = threading.Thread(target = test_thread())
			test_thread.start() # --> dont do this here, do this thread inside of a callback function
			# root.bind('<Map>', start_thread)
			firstRun = False

	# GUI_Thread = threading.Thread(target = root.mainloop())
	# GUI_Thread.start()


	# GUI_Thread.join()
	# test_thread.join()
