import numpy as np
import sys

#define a function that returns a value
def expo(x):
	return np.exp(x)

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))

#defing a main function
def main():
	n = 10

	#check if there a is a command line argument provided
	if(len(sys.argv)>1):
		n = int(sys.argv[1])

	show_expo(n)


if __name__ == '__main__':
	main()