from tkinter import ttk, Tk, LabelFrame, StringVar, OptionMenu
from DataManager import DataManager
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from GUI.Plot import Plot
from GUI.Table import Table


class MainMenuGUI:

	def __init__(self):
		self.root = Tk()
		self.frame1 = None
		self.frame2 = None
		self.frame3 = None
		self.table = Table()
		self.plot = Plot()
		self.start()

	def start(self):
		self.root.title('Cryto analyser - DK & BO')
		self.root.geometry('800x800')
		self.init_frames()
		self.init_drop_down_cr()
		self.table.treeview = ttk.Treeview(self.frame2, style="Treeview")
		self.update_plot()
		self.root.mainloop()

	def init_frames(self):

		""" Creates frames that help position GUI elements """

		# frame1 exist in row=0 and contain widgets to interaction with user: dropdown menu, slider, buttons ...
		# frame2 exist in row=1 and contain Treeview with data
		# frame3 exist in row=2 column=0 and contain timeseries plot

		self.frame1 = LabelFrame(self.root, padx=5)
		self.frame1.grid(row=0, column=0)
		self.frame2 = LabelFrame(self.root, padx=5)
		self.frame2.grid(row=1, column=0, columnspan=2)
		self.frame3 = LabelFrame(self.root, padx=5)
		self.frame3.grid(row=2, column=0)

	def init_drop_down_cr(self):
		selected_currency = StringVar()
		selected_currency.set(DataManager.available_cr[0])
		drop_down_cr = OptionMenu(self.frame1, selected_currency, *DataManager.available_cr, command=self.change_data)
		drop_down_cr.config(width=20)
		drop_down_cr.grid(row=0, column=0)

	def change_data(self, cr):
		self.table = Table(cr)
		self.plot = Plot(cr)
		self.update_plot()

	def update_plot(self):
		self.frame3 = LabelFrame(self.root, padx=5)
		self.frame3.grid(row=2, column=0)
		self.plot.figure_canvas = FigureCanvasTkAgg(self.plot.figure_mpl, master=self.frame3)
		self.plot.figure_canvas.get_tk_widget().pack()
		self.plot.figure_canvas.draw()





