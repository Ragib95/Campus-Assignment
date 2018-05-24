def divide(x, y):
	try:
		result = x / y
		return result
		
	except ZeroDivisionError:
		raise


if __name__== "__main__":
	a,b = map(int, raw_input().split())
	result = divide(a,b)
	print result
