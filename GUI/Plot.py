from matplotlib.figure import Figure
from DataManager import DataManager


class Plot:
	figure_mpl = None
	figure_canvas = None

	def __init__(self, cr=None):
		Plot.figure_mpl = Figure(figsize=(7,5))
		dataframe = DataManager.get_data_to_treeview(cr)
		self.get_timeseries_plot(dataframe, cr)

	@staticmethod
	def get_timeseries_plot(dataframe, cr):
		a = Plot.figure_mpl.add_subplot(111)
		a.scatter(dataframe.timestamp, dataframe.close)

		a.set_title(f'{cr} price in USD', fontsize=16)
		a.set_ylabel('Price [USD]', fontsize=14)
		a.set_xlabel('Date', fontsize=14)