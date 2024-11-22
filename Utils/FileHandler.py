import csv

def csvs_to_dicts(filelist):
	output = {}
	for file in filelist:
		csv_file_path = f"./csv/{file}.csv"
		with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
			lines = csv_file.readlines()
			header = lines[1].strip().split(",")
			reader = csv.DictReader(lines[3:], fieldnames=header)
			file_data = {}
			for row in reader:
				key = row.pop('#', None)
				if key is not None:
					file_data[key] = row
			output[file] = file_data
	return output