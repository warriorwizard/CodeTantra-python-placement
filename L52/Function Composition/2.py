def compose(*functions):
	def inner(arg):
		for f in reversed(functions):
			arg =f(arg)
		return arg
	return inner
def square(x):
	return x**2
def increment(x):
	return x+1
def half(x):
	return x/2
composed = compose(square, increment, half)
print(composed(5))
# square(increment(half(x)))
composed=compose(square, increment)
print(composed(5))
	
		