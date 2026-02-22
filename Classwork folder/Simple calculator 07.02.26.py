m=input('Enter the first number:')
print((type(m)))
m=int(m)
print((type(m)))
n=int(input("Enter the second number:"))
print((type(n)))
print(f'The numbers you have entered are {m} and {n} ')
print("This is a simple calculator")
print('press A for addition')
print('press S for subtraction')
print('press M for multiplication')
print('press D for division')
variable=input('Select a letter from any of the above options:')
if variable=='A':
	print(m+n)
elif variable=='S':
	print(m-n)
elif variable=='M':
	print(m*n)
elif variable=='D':
	print(m/n)
else:
	 print('You have entered an invalid option.')