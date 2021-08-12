from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import threading
from Test_File import TestThread

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


# What grid should look like:
# 	col 0		col 1		col 2		col 3
# -----------------------------------------------
# |			|			|			|			|	row 0
# |			|			|			|			|
# -----------------------------------------------
# |			|			|			|			|	row 1
# |			|			|			|			|
# -----------------------------------------------
# |			|			|			|			|	row 2
# |			|			|			|	     	|
# -----------------------------------------------

class GUI_Functions():

	def __init__(self, root):

		root.geometry("800x700")

		# elements for the first section of the window grid
		self.section_1 = Label(root, text="This is the first section of the window.\n [This is where the camera image will be loaded]", bg="MediumPurple1").grid(column=0, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)

		# elements for the second section of the window grid
		self.section_2 = Label(root, text="This is the second section of the window.\n [This is where the simulation will be visible]", bg="SteelBlue2").grid(column=2, row=0, columnspan=2, rowspan=2, sticky=N+E+S+W)
		self.add_object_btn = Button(root, text="Add object", command=self.add_objects_clicked).grid(column=2, row=1, sticky=S, pady=15)
		self.remove_obejct_btn = Button(root, text="Remove object", command=self.remove_objects_clicked).grid(column=3, row=1, sticky=S, pady=15)
		self.holder = Label(root, text="This is a holder for where the simulation will be displayed.", bg="White").grid(column=2, row=0, columnspan=2, rowspan=1, sticky=N+E+S+W, padx=20, pady=20)

		# elements for the third section of the window grid
		self.section_3 = Label(root, text="This is the third section of the window.\n [This will remain empty for now]", bg="Orchid2").grid(columnspan=4, row=2, sticky=N+E+S+W)

		thread_1 = threading.Thread(TestThread())
		thread_1.start()

		self.section_1.text = thread_1

		# configuring columns and rows
		Grid.columnconfigure(root, 0, weight=1)
		Grid.columnconfigure(root, 1, weight=1)
		Grid.columnconfigure(root, 2, weight=1)
		Grid.columnconfigure(root, 3, weight=1)
		Grid.rowconfigure(root, 0, weight=1)
		Grid.rowconfigure(root, 1, weight=1)
		Grid.rowconfigure(root, 2, weight=1)

	# uses a thread to load camera image code separate from the GUI window
	def load_camera_image(self):
		pass

	# displays the simulation 
	def show_simulation(self):
		pass

	# handles the event where the 'add objects' to simulation button is clicked
	def add_objects_clicked(self):
		pass

	# handles the event where the 'remove objects' from simulation button is clicked
	def remove_objects_clicked(self):
		pass

if __name__ == '__main__':
	root = Tk()
	root.title('Lab GUI Window')
	gui_fun = GUI_Functions(root)
	root.mainloop() 

	
