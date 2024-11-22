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
			'ClassJobCategory'
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
			"Requires" : RequiredClasses
		}

	print(output['4005'])
