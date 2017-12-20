import json
import difflib

# convert the json into a Python Dictionary
our_dict = json.load(open("data.json",'r'))
our_keys = our_dict.keys() # only build this once (not per query)

def look_up(q):
	if q in our_keys:
		# Tell the user if there are multiple definitions.
		if len(our_dict[q]) > 1:
			print("Found multiple definitions for %s:" % q)
		else:
			print("Found this definition for %s:" % q)

		for ans in our_dict[q]:
			print("-> " + ans) # separate definitions by lines and '->'

	# Interactively attempt to determine what the user meant.
	else: 
		close_matches = difflib.get_close_matches(q, our_keys, 6)

		# Check the closest keyed word to the query
		print("Unable to find a definition for %s..." % q)
		response = input("Did you mean %s? [Y/N]" % close_matches[0]).lower()

		if response[0] == "y":
			look_up(close_matches[0])

		# Give the user a few more options
		else:
			print("Did you mean one of these words?")
			for i in range(1,len(close_matches)):
				print(str(i) + ": "+close_matches[i])
			print("Type the number of the intended word," +
				" or any other number to retry.")
			response = input(">>")

			# User properly identifies a suggested alternative
			if int(response) in range(1,6):
				look_up(close_matches[int(response)])

			# Give up.
			else:
				print("Check your input and try inputting a new word.")

while True: 
	# get the word in all lowercase
	query = input("Please input a word: ").lower() 
	look_up(query)
