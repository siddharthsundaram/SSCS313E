
import math
# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
def encrypt ( strng ):
	length = len(strng)
	side = 1
	while length > side ** 2: side += 1
	arr = [["" for i in range(side)]for j in range(side)]
	ind = 0
	for i in range(side):
		for j in range(side):
			if ind < length:
				arr[i][j] = strng[ind]
				ind += 1
			else:
				arr[i][j] = "*"
	#for r in arr: print(r)
	#print()
	new = [["" for i in range(side)]for j in range(side)]
	for i in range(side):
		for j in range(side):
			new[j][side-1-i] = arr[i][j]
	str = ""
	for l in range(side):
		for m in range(side):
			str += new[l][m]
	str=str.replace("*", "")
	print(str)



# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
def decrypt ( strng ):

	# This section determines the dimensions of the 2d array
	length = len(strng)
	side = 1
	while length > side ** 2: side += 1

	# Determines how many spaces will be filled with *s
	whitespace = (side**2) - length

	# Fills spaces with *s so that they are at the end of the 2d list after getting rotated 90 deg ccw (bottom to top, left to right)
	count = 0
	temp = [["" for i in range(side)]for j in range(side)]
	for i in range(side):
		for j in range(side):
			if count < whitespace:
				temp[side-1-j][i] = "*"
				count += 1
			else: break

	# Fills in the characters of the string into the array where there aren't already *s (left to right, top to bottom)
	strcount = 0
	for i in range(side):
		for j in range(side):
			if temp[i][j] != "*":
				temp[i][j] = strng[strcount]
				strcount += 1

	# Creates new array that rotates the previous one 90 degrees counterclockwise
	new = [["" for i in range(side)]for j in range(side)]
	for i in range(side):
		for j in range(side):
			new[i][j] = temp[j][side - 1 - i]

	# Reads the 2d array left to right, top to bottom and puts the characters into a string (not the *s) and prints
	str = ""
	for l in range(side):
		for m in range(side):
			str += new[l][m]
	str=str.replace("*", "")
	print(str)

def main():
	encrypt(str(input()))
	decrypt(str(input()))


if __name__ == "__main__":
	main()
