import random

def main():
	print("Matthew Polgar")
	x = random.randint(0, 100)
	y = random.randint(0, 100)
	print(x)
	print(y)
	print("Sum = %d" % (x+y))
	print("Average = %g" % ((x+y)/2))

if __name__ == "__main__":
	main()
