class Abstract(object):
	def foo(self):
		raise NotImplementedError('subclasses must override foo()!')
class Derived(Abstract):
	def foo(self):
		print('Hooray!')
d = Derived()
d.foo()