# Considering the code below, write code that prints out True! if the last 3 characters of the string are all digits and prints out false! otherwise
# Hint! Use the appropirate method to check if the requested string slice contains digits only
x = "The days of python 2 are almost over, Python 3 is the king now." 
if x[-3:].isdigit():
	print("True!")
else:
	print("False!")