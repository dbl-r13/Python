#We will be writing a module with this code

def extract_upper(phrase):
	return list(filter(str.isupper, phrase))

def extract_lower(phrase):
	return list(filter(str.islower, phrase))



