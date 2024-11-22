import csv
import json

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

	with open(f"./patchlist.json", 'r', encoding='utf-8') as sfile:
		patchlist_raw = json.load(sfile)
		patchlist = {str(item["ID"]): item["Version"] for item in patchlist_raw}

	for file in output:
		with open(f"./patchdata/{file}.json", 'r', encoding='utf-8') as sfile:
			patchdata = json.load(sfile)

		for key in output[file]:
			strkey = str(key)
			if strkey in patchdata:
				v = str(patchdata[strkey])
				output[file][strkey]['patchversion'] = patchlist.get(v, "0.0")

	return output