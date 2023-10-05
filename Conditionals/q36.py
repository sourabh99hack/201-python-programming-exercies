# Considering the code below, write the code that prints out True! if at least one of the following conditions occurs:
# - the string contains the character z
# - the string contains teh character y at least twice.
x = "The days of python 2 is over. Python 3 is the king now"
if "z" in x or x.count("y") >= 2:
	print("True")