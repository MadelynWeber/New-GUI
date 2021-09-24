from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import threading
import time
from Test_File import TestThread
import concurrent.futures

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
		self.placeholder = Label(root, text="This is a placeholder for where the simulation will be displayed.", bg="White", width=15, height=30).grid(column=2, row=0, columnspan=2, rowspan=1, sticky=N+E+S+W, padx=20, pady=20)


		# make self.placeholder here be the loaded simulatin.py file


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
		lbl = Label(self.add_window, text="Enter the values for an object to add.").pack()
		e = Entry(self.add_window, width=20).pack()
		add_btn = Button(self.add_window, text="Add", command=self.add_btn_clicked).pack()
		cancel_btn = Button(self.add_window, text="Cancel", command=lambda: self.cancel_btn_click(self.add_window)).pack()

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

	def add_btn_clicked(self):
		# do stuff for when "add" object button is clicked
		print("** Add button clicked **")

	def remove_btn_clicked(self):
		# do stuff for when "remove" object button is clicked
		print("** Remove button clicked **")



	# function to test updates to GUI window
	def test_updates(self, value_of_update):

		print("---> Is in test_updates function")

		#self.section_1 = Label(root, text=value_of_update)
		self.section_1.config(text=value_of_update)
		self.section_1.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)

		self.section_1.update()

def test_thread():
	print("---> Before executor...")
	with concurrent.futures.ThreadPoolExecutor() as executor:
		future = executor.submit(TestThread)
		return_value = future.result()

	print("---> before test_updates...")
	# try to update the GUI window with new text value
	gui_fun.test_updates(return_value)
	print("---> after test_updates...")



if __name__ == '__main__':
	print("running... ")
	root = Tk()
	root.title('Lab GUI Window')
	gui_fun = GUI_Functions(root)
	# root.mainloop() 

	# NOTE:
	# if mainloop() is called first, then it runs the tkinter window and not the thread below
	# if the thread below is called before mainloop(), then it runs the code in the thread first, then opens the tkinter window with the updates from the code second

	# this works to run the other code and update the GUI window.. but doesn't run at the same time as the tkinter window - loads this first, then the window
	print("starting  thread...")
	test_thread = threading.Thread(target = test_thread())
	test_thread.start()

	root.mainloop()


	# GUI_Thread = threading.Thread(target = root.mainloop())
	# GUI_Thread.start()


	GUI_Thread.join()
	test_thread.join()

	
