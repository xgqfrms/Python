
num = int(input())


def fibonacci(n):
	#complete the recursive function
	if(n == 0 ):
		return 0
	elif(n == 1 or n == 2):
		return 1
	else:
		return (fibonacci(n - 1) + fibonacci(n - 2))

i = 0;
while(i < num):
	print(fibonacci(i))
	i += 1
