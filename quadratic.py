from matplotlib import pyplot as plt 
from matplotlib import style
import numpy as np

plt.style.use("fivethirtyeight")
class Quadratics():
	def __init__(self,*args):
		lx = []
		for input_given in args:
			lx.append(input_given)
		lx.reverse()		
		self.constant=lx[0]
		self.coeff_x=lx[1]
		self.coeff_x_sq=lx[2]
		
	def grapher(self):
		X = np.array(range(100))
		Y = X**2 
		plt.plot(X , Y , label = "y = X^2" ,linewidth=2 , linestyle="-")
		plt.title("A simple graph for simple functions ")
		plt.ylabel("Y - axis")
		plt.xlabel("X- axis")
		plt.grid(False)
		plt.tight_layout()
		plt.show()
	def print_eq(self):
		return f"The equation is as follows: {self.coeff_x_sq}x^2 + {self.coeff_x}x + {self.constant}"
	def roots(self):
		p= -self.coeff_x + (self.coeff_x**2 - 4*self.coeff_x_sq*self.constant)**0.5
		global r1
		r1 = p / 2*self.coeff_x_sq
		q = -self.coeff_x - (self.coeff_x**2 - 4*self.coeff_x_sq*self.constant)**0.5
		global r2
		r2 = q / 2*self.coeff_x_sq
		return f" Roots of the equation are: \"{r1} \" and \"{r2}\" "
a,b,c = int(input("Enter Coefficient of X square")) , int(input("Enter Coefficient of  X")) , int(input("Enter constant"))
eq1  = Quadratics(a ,b ,c)
print(eq1.print_eq())
print(eq1.roots())
print('The graph is as follows:')
print("Coming soon")
eq1.grapher()

