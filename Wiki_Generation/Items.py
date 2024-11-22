from Utils.FileHandler import csvs_to_dicts
from Utils.Common import str_replace_characters

def gen_items():
	bad_character_search = ["–", "—", "<Emphasis>", "</Emphasis>", "''", "?", "#", "[", "]"]
	bad_character_replace = ["-", "-", None, None, None, None, "", "(", ")"]
	def bad_char_fix(_string):
		return str_replace_characters(bad_character_search,bad_character_replace,_string)
	Data = csvs_to_dicts(
		[
			'Item', 
			'ItemUICategory', 
			'ClassJobCategory',
			'ClassJob'
		]
	)
	output = {}
	for id, item in Data['Item'].items():
		if item['patchversion'] == "0.0" : continue
		FitsGM = None
		if item['Description'] == "Fits: Game Masters":
			FitsGM = "Game Masters"
		Slots = None
		advancedmelding = None
		if int(item['MateriaSlotCount']) > 0:
			Slots = item['MateriaSlotCount']
			if item['IsAdvancedMeldingPermitted'] == "False":
				advancedmelding = "No"
		stack = None
		if int(item['StackSize']) > 1:
			stack = item['StackSize']
		RequiredClasses = None
		if int(item['ClassJobCategory']) > 0:
			RequiredClasses = Data['ClassJobCategory'].get(item['ClassJobCategory'],'').get("Name","")
		untradable = None
		if item['IsUntradable'] == "True":
			untradable = "Yes"
		unique = None
		if item['IsUnique'] == "True":
			unique = "Yes"

		Repair = None
		Extractable = None
		excluded_categories = {
			33, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
			61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 
			79, 80, 81, 82, 83, 85, 86, 90, 91, 92, 93, 94, 95, 100, 101, 102, 103, 104
		}
		if (item['ClassJob{Repair}'] == "0" or int(item['ItemUICategory']) in excluded_categories):
			Extractable = "No"
		else:
			class_job_name = Data['ClassJob'].get(item['ClassJob{Repair}'], {}).get('Name', "")
			Repair = class_job_name.title()
			
			if int(item['MaterializeType']) > 0:
				Extractable = "Yes"
			else:
				Extractable = "No"

		Damage = None
		

		output[id] = {
			"Patch" : item['patchversion'],
			"Index" : id,
			"Rarity" : item['Rarity'],
			"Name" : bad_char_fix(item['Name']),
			"Subheading" : bad_char_fix(Data['ItemUICategory'].get(item['ItemUICategory'],'').get('Name',"")),
			"Description" : item['Description'],
			"FitsGM" : FitsGM,
			"Slots" : Slots,
			"Advanced Melds" : advancedmelding,
			"Stack" : stack,
			"Requires" : RequiredClasses,
			"Required Level" : item['Level{Equip}'],
			"Item Level" : item['Level{Item}'],
			"Untradable" : untradable,
			"Unique" : unique,
			"Extractable" : Extractable,
			"Repair" : Repair,
		}

	print(output['4013'])
