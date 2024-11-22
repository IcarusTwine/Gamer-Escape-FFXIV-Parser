from Utils.FileHandler import csvs_to_dicts

def gen_items():
	Data = csvs_to_dicts(['Item','EventItem'])
	print(Data['Item']['40282'])
