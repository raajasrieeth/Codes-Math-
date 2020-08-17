from functools import lru_cache
import math
import time
class Pythagoras():
	def __init__(self , first_num , second_num):
		self.opposite =  first_num
		self.adjacent = second_num
		self.hypotenuse = math.sqrt(self.opposite**2+self.adjacent**2)

	def make_third_side (self):
		'''returns the length of the third possible side'''
		# a = int(input("Enter a number"))
		# b = int(input("Enter  the second number"))
		c = self.hypotenuse
		return c 
	@lru_cache(maxsize=2)
	def trig_ratios(self , ratio):
		'''the angle is taken as wrt to the init method , therefore for the other angle , use the inverted functions(below)]
		sine --> cosine
		cosine --> sine
		tan --> cot
		cot --> tan
		sec --> cosec
		cosec --> sec
		'''
		sine_theta = self.opposite/self.hypotenuse
		cos_theta = self.adjacent/self.hypotenuse
		tan_theta = sine_theta/cos_theta
		try:
			if "sin" in ratio: return sine_theta
			elif "cos" in ratio:return cos_theta
			elif "tan" in ratio: return tan_theta
			elif "cot" in ratio:return tan_theta**-1
			elif "cosec" in ratio:return sine_theta**-1
			elif "sec" in ratio:return cos_theta**-1
			else:  return "What are you entering??"
		except NameError:
			return "Please enter as a string"
	def make_triplets(self):
		a = float(input("Enter one number"))
		b = float(input("Enter another number"))
		return "{} , {} and {} form a Pythagorean triplet.".format(a , b , math.sqrt(a**2 + b**2))
tri = Pythagoras(3,4)	
# print(tri.trig_ratios("sec"))
# print(tri.make_triplets())


		

	