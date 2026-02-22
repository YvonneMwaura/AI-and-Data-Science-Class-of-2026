#Saturday 21st February 2026
state=0.55
quo=10
name='youtube'
print(type(state),type(quo),type(name))
print(type(state))
print((type(quo)))
print((type(name)))
print(f'hello {name}, the amount of money you have is {quo} shillings and {state} cents')
if quo>=20:
    print('You have above sufficient money')
elif quo>=50:
	print('You have below sufficient money')
else:
	print('invalid option')
#Ternary operator
AgeChecker='Adults' if quo>=18 else 'Child'
print(AgeChecker)
#Same code as the one above
if quo>=18:
	AgeChecker='Adult'
else:
	AgeChecker='Child'
print(AgeChecker)