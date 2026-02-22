name=input('Hello ,welcome.What is your name?')
YOB=int(input('Enter your year of birth'))
age=(2026-YOB)
if age>=18:
	print(f'You are welcome to our site,you are eligible to enter since you are{age} years old.')
else:
	print(f'You have been banned from our site.You are not eligible to enter since you are {age} years old')