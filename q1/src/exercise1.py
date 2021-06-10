"""
Module that abstracts a
pizzeria
"""

class PizzaComponent:
	"""
	Abstract component in the
	decorator design pattern
	"""
	def getName(self):
		"""
		returns a descriptive name for
		the class
		"""
		return self.__class__.__name__
	def getCost(self):
		"""
		returns its cost
		"""
		return self.__class__.cost

class PizzaDough(PizzaComponent):
	"""
	Concrete component in the
	decorator design pattern
	"""
	cost = 0.0

class Decorator(PizzaComponent):
	"""
	Abstract decorator class in
	the decorator design pattern
	"""
	def __init__(self, pizzaComponent):
		"""
		Initializes wrapping another
		pizza component
		"""
		self.component = pizzaComponent
	
	def getName(self):
		"""
		Returns its name added to its wrapped component's
		name
		"""
		return self.component.getName() + ' ' + PizzaComponent.getName(self)
	
	def getCost(self):
		"""
		Returns its cost added to its wrapped component's
		cost
		"""
		return self.component.getCost() + PizzaComponent.getCost(self)

# The following classes are all concrete decorators
# in the decorator design pattern

class Sausage(Decorator):
	"""
	A sausage ingredient for pizza
	"""
	cost = 6.5

class Cheese(Decorator):
	"""
	A cheese ingredient for pizza
	"""
	cost = 5

class Meat(Decorator):
	"""
	A meat ingredient for pizza
	"""
	cost = 8

class Ham(Decorator):
	"""
	A ham ingredient for pizza
	"""
	cost = 5

class Oregano(Decorator):
	"""
	A oregano ingredient for pizza
	"""
	cost = 3.5

class Egg(Decorator):
	"""
	An egg ingredient for pizza
	"""
	cost = 5

portuguese = Cheese(Ham(Oregano(Egg(PizzaDough()))))
print('portuguese pizza data:')
print('descriptive name: ' + portuguese.getName())
print('cost: ' + str(portuguese.getCost()))

meaty = Sausage(Meat(Oregano(Egg(PizzaDough()))))
print('meaty pizza data:')
print('descriptive name: ' + meaty.getName())
print('cost: ' + str(meaty.getCost()))

