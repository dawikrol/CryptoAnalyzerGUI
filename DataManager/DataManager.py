from os import listdir
import pandas as pd


def find_extension_filenames(path, extension='.csv'):
	filenames = listdir(path)
	return [filename for filename in filenames if filename.endswith(extension)]


available_cr = find_extension_filenames(path=r'.\Data')


def get_dataframe(file):
	data_fr = pd.read_csv(file, usecols=['timestamp', 'open', 'high', 'low', 'close'])
	data_fr['timestamp'] = pd.to_datetime(data_fr['timestamp'], format='%Y-%m-%d')
	return data_fr


def get_data_to_treeview( cr=None):
	if cr is None:
		cr = available_cr[0]
	cr_df = get_dataframe(fr'.\Data\{cr}')
	return cr_df

