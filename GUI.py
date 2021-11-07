from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import threading
import time
from Test_File import TestThread
import concurrent.futures
import sys
sys.path.insert(1, '../pythonCamera')
from start import test_function
#sys.path.insert(1, '../pythonSimulator')
#from example import test_put_obstacle
#sys.path.insert(1, '../pythonSimulator')
#from pythonSimulator.start import return_image
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

		root.geometry("2560x1440")

		# elements for the first section of the window grid
		self.section_1 = Label(root, text="Loading Camera Image...", bg="MediumPurple1")
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
		Grid.rowconfigure(root, 0, weight=1)
		Grid.rowconfigure(root, 1, weight=0)
		Grid.rowconfigure(root, 2, weight=4)

		self.objects_dict = {}		# dictionary to hold added objects

	# function to update GUI window by displaying the 'frame' object found from (D:Workspace/pythonCamera/start.py)
	def load_camera_image(self):
		while True:
			returned_val = test_function()

			# print("type of return value: ", type(returned_val)) # --> type is: numpy.ndarray

			# array = np.ones((500, 500))*150

			img = ImageTk.PhotoImage(image = Image.fromarray(returned_val))
			
			self.section_1.config(image=img)
			self.section_1.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
			self.section_1.update()

			# print("width: ", root.winfo_screenwidth())
			# print("height: ", root.winfo_screenheight())


	# displays the simulation 
	def show_simulation(self):
		# TODO: figure out how to embed the arcade window in this GUI window
		image = return_image()
		pass

	# handles the event where the 'add objects' to simulation button is clicked
	def add_objects_clicked(self):
		self.add_window = Toplevel(root)
		self.add_window.geometry("400x400")
		self.add_window.title("Add Object")

		lbl = Label(self.add_window, text="Enter the values for an object to add.").grid(column=0, row=0)
		name_lbl = Label(self.add_window, text="Enter a name for the object: ").grid(column=0, row=1)
		self.add_window.object_name = Text(self.add_window, height=1, width=15)
		self.add_window.object_name.grid(column=1, row=1)
		x_lbl = Label(self.add_window, text="Enter an x-value: ").grid(column=0, row=2)
		self.add_window.x_val = Text(self.add_window, height=1, width=15)
		self.add_window.x_val.grid(column=1, row=2)
		y_lbl = Label(self.add_window, text="Enter a y-value: ").grid(column=0, row=3)
		self.add_window.y_val = Text(self.add_window, height=1, width=15)
		self.add_window.y_val.grid(column=1, row=3)
		angle_lbl = Label(self.add_window, text="Enter an angle value: ").grid(column=0, row=4)
		self.add_window.angle_val = Text(self.add_window, height=1, width=15)
		self.add_window.angle_val.grid(column=1, row=4)
		width_lbl = Label(self.add_window, text="Enter a width value: ").grid(column=0, row=5)
		self.add_window.width_val = Text(self.add_window, height=1, width=15)
		self.add_window.width_val.grid(column=1, row=5)
		height_lbl = Label(self.add_window, text="Enter a height value: ").grid(column=0, row=6)
		self.add_window.height_val = Text(self.add_window, height=1, width=15)
		self.add_window.height_val.grid(column=1, row=6)

		add_btn = Button(self.add_window, text="Add", command=lambda: self.add_btn_clicked(self.add_window.object_name, self.add_window.x_val, self.add_window.y_val, self.add_window.angle_val, self.add_window.width_val, self.add_window.height_val))
		add_btn.grid(column=0, row=7)
		cancel_btn = Button(self.add_window, text="Cancel", command=lambda: self.cancel_btn_click(self.add_window))
		cancel_btn.grid(column=2, row=7)


	# handles the event where the 'remove objects' from simulation button is clicked
	def remove_objects_clicked(self):
		self.remove_window = Toplevel(root)
		self.remove_window.geometry("400x400")
		self.remove_window.title("Remove Object")

		lbl = Label(self.remove_window, text="Enter the name of the object to remove.").grid(column=0, row=0)
		self.remove_window.remove_object = Text(self.remove_window, height=1, width=15)
		self.remove_window.remove_object.grid(column=1, row=1)
		# e = Entry(self.remove_window, width=20).pack()
		remove_btn = Button(self.remove_window, text="Remove", command=self.remove_btn_clicked).grid(column=0, row=2)
		cance_btn = Button(self.remove_window, text="Cancel", command=lambda: self.cancel_btn_click(self.remove_window)).grid(column=2, row=2)

	def cancel_btn_click(self, window_to_close):
		print("** button clicked to cancel **")
		window_to_close.destroy()
		window_to_close.update()

	def add_btn_clicked(self, name, x, y, angle, width, height): 

		print("** add button has been clicked **")
		
		# getting objects entered into text boxes
		object_name = self.add_window.object_name.get("1.0", 'end-1c')
		object_x_val = self.add_window.x_val.get("1.0", 'end-1c')
		object_y_val = self.add_window.y_val.get("1.0", 'end-1c')
		object_angle_val = self.add_window.angle_val.get("1.0", 'end-1c')
		object_width_val = self.add_window.width_val.get("1.0", 'end-1c')
		object_height_val = self.add_window.height_val.get("1.0", 'end-1c')
		
		# removing values entered into text boxes
		self.add_window.object_name.delete("1.0", 'end-1c')
		self.add_window.x_val.delete("1.0", 'end-1c')
		self.add_window.y_val.delete("1.0", 'end-1c')
		self.add_window.angle_val.delete("1.0", 'end-1c')
		self.add_window.width_val.delete("1.0", 'end-1c')
		self.add_window.height_val.delete("1.0", 'end-1c')

		print("TESTING VALUES: ", object_name, object_x_val, object_y_val, object_angle_val, object_width_val, object_height_val)

		self.add_window.destroy()
		self.add_window.update()

	def remove_btn_clicked(self):

		print("** Remove button clicked **")

		self.remove_window.remove_object.delete("1.0", 'end-1c')

		self.remove_window.destroy()
		self.remove_window.update()



	# function to test adding an image to the GUI window
	# def test_add_image(self):

	# 	self.image_1 = Image.open("./image_2.jpeg").resize((400, 200))
	# 	self.img_1 = ImageTk.PhotoImage(self.image_1)

	# 	self.section_1.config(image=self.img_1)
	# 	self.section_1.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
	# 	self.section_1.update()

	# function to test updates to GUI window
	# def test_updates(self, value_of_update):

	# 	print("---> Is in test_updates function")

	# 	#self.section_1 = Label(root, text=value_of_update)
	# 	self.section_1.config(text=value_of_update)
	# 	self.section_1.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)

	# 	self.section_1.update()

		#self.test_add_image()



def test_thread():
	# print("---> Before executor...")
	with concurrent.futures.ThreadPoolExecutor() as executor:
		future = executor.submit(TestThread)
		return_value = future.result()

	# print("---> before test_updates...")
	# try to update the GUI window with new text value
	# gui_fun.test_updates(return_value)
	# print("---> after test_updates...")

	image_to_display = gui_fun.load_camera_image()

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
