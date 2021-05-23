from DataManager import DataManager
from tkinter import ttk, Tk, LabelFrame, StringVar, OptionMenu


class Table:

	treeview = None

	def __init__(self, cr=None):
		self.init_treeview(cr)

	def init_treeview(self, cr):
		treeview = ttk.Treeview()
		dataframe = DataManager.get_data_to_treeview(cr)
		style = ttk.Style()
		style.theme_use("clam")
		style.configure("Treeview", background="gray", foreground="black", rowheight=20, filedbackground="blue")
		style.map("Treeview", background=[('selected', 'red')])
		treeview['columns'] = list(dataframe.columns)
		for col in list(dataframe.columns):
			treeview.column(col, anchor='w')
			treeview.heading(col, text=col, anchor='w')
		for index, row in dataframe.iterrows():
			treeview.insert("", 0, text=index, values=list(row))
		treeview.grid(row=1, column=0)
		Table.treeview = treeview