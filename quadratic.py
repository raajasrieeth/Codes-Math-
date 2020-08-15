from matplotlib import pyplot as plt 
from matplotlib import style
import numpy as np

plt.style.use("fivethirtyeight")

class Quadratics():
	'''This class contains all methods pertaining to quadratic equations.'''
	def __init__(self,*args):
		lx = []

		for input_given in args:
			lx.append(input_given)

		self.constant=lx[2]
		self.coeff_x=lx[1]
		self.coeff_x_sq=lx[0]
		
	def grapher(self):
		'''graphs the quadratic'''
		start = -10  # the width of the graph
		stop  = 10

		X = np.linspace(start , stop , 100)# a 100 numbers between the range

		plt.xlim((start,stop))
		plt.ylim(start , stop)

		axis = plt.gca()# get current axis

		plt.plot(axis.get_xlim() , [0,0] , color="k" , linestyle="--" , linewidth = 1)#makes the x axis
		plt.plot([0,0] ,axis.get_ylim() , color="k" ,linestyle="--" ,linewidth = 1)#makes the y axis

		plt.plot(X , self.coeff_x_sq*(X**2) + self.coeff_x*X +self.constant , label = "Your graph" ,linewidth=2 , linestyle="-")# the real deal

		plt.title("Your Graph ")
		plt.ylabel("Y - axis")
		plt.xlabel("X- axis")

		plt.grid(False)
		plt.tight_layout()

		plt.show()


	def print_eq(self):
		'''prints the equation'''
		return f"The equation is as follows: {self.coeff_x_sq}x^2 + {self.coeff_x}x + {self.constant}"


	def roots(self):
		'''responsible for calculating the roots. '''
		p= -self.coeff_x + (self.coeff_x**2 - 4*self.coeff_x_sq*self.constant)**0.5
		global r1
		r1 = p / (2*self.coeff_x_sq)

		fraction_1 = f'[-{self.coeff_x} + sqrt({(self.coeff_x**2 - 4*self.coeff_x_sq*self.constant)})]/{self.coeff_x_sq*2}'

		q = -self.coeff_x - (self.coeff_x**2 - 4*self.coeff_x_sq*self.constant)**0.5
		global r2
		r2 = q /(2*self.coeff_x_sq)

		fraction_2 = f'[-{self.coeff_x} - sqrt({(self.coeff_x**2 - 4*self.coeff_x_sq*self.constant)})]/{self.coeff_x_sq*2}'

		return f" Roots of the equation are: \"{r1} \" and \"{r2}\" ; fractional form:{fraction_1} ; {fraction_2}"

class Cubics():
	'''deals with cubic expressions'''
	def __init__(self,*args):
		lc = list(x for x in args)
		self.coeff_x_cub = lc[0]
		self.coeff_x_squ = lc[1]
		self.coeff__x = lc[2]
		self.const = lc[3]

	def printEq(self):
		'''returns the polynomial's form '''
		return f"You polynomial is as follows: {self.coeff_x_cub}x^3 + {self.coeff_x_squ}x^2 + {self.coeff__x}x + {self.const}"
	def roots(self):
		'''makes the roots of the cubic polynomial'''
		pass
	def grapher(self):
		'''makes the graph'''
		pass
a,b,c = int(input("Enter Coefficient of X square\t")) , int(input("Enter Coefficient of  X\t")) , int(input("Enter constant\t"))

eq1  = Quadratics(a ,b ,c)
print(eq1.print_eq())
print(eq1.roots())
print('The graph is as follows:')
print("Work in progress for imaginary roots! (exceeding 10)")
eq1.grapher()

