"""
@author sagarGhimire
"""
#!/bin/python3
import math
import sys

print(sys.version)

class Square(object):
	"""
	Class Square takes side length of a square from user input
	Capable of calculating area and perimeter
	Valid inputs: positive real numbers, >= 0
	Character 'n' is used to quit
	"""
	def __init__(self, side_length=0):
		self.set_side_length(side_length)

	def set_side_length(self, len):
		"""
		Call to set the side length
		Created the function so I don't have to create new object everytime
		:param len: input form user
		:return: valid side lengths
		"""
		# check for non integer input
		try:
			self.side_length = float(len)
		except:
			self.side_length = 0
		self.side_length = self.check_type(self.side_length)

	def square_area(self):
		"""
		Function to calculate the area of the square
		:return: int
		"""
		return self.side_length ** 2

	def square_perimeter(self):
		"""
		Functiion to calculate the perimeter of the square
		:return: int
		"""
		return 4*self.side_length

	def check_type(self, side_lenght):
		"""
		Check for non alphabetic valid values
		Since float is not a requirement, this function converts every number to integer
		if negative, return 0
		if > 10 , return 0
		:param side_lenght: user input side length
		:return: int
		"""
		if side_lenght > 10:
			print("[WARNING] Side length should be in between 0 and 10. Using 0 for side length.")
			return 0
		else:
			return math.floor(side_lenght) if side_lenght >= 0 else 0

	def __str__(self):
		"""
		:return: Standard output for the object
		"""
		return ("The square with length %d has an area of %d units and perimeter of %d units." %(self.side_length, self.square_area(), self.square_perimeter()))


if __name__=='__main__':
	len = input("Enter your square length: ")
	newSquare = Square(len)
	print(newSquare)
	while len != 'n':														# run until quit
		len = input("Enter your square length (input 'n' to exit): ")
		if len == 'n': break
		newSquare.set_side_length(len)
		print(newSquare)
	print("Thanks for having a good time.")