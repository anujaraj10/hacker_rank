# 1-find the factorial of the number:

# def factorial(n):
# 	if n == 0:
# 		return 1
# 	else:
# 		return n*factorial(n-1)	
# n = int(raw_input(''))		
# print factorial(n)


# 2-fibonacci number
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)
n = int(raw_input(''))
print fib(n)