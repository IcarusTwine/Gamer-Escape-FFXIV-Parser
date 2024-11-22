def str_replace_characters(search, replace, text):
	for s, r in zip(search, replace):
		if r is None:  # If the replacement is None, remove the string
			text = text.replace(s, "")
		else:
			text = text.replace(s, r)
	return text