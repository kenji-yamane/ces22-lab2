from abc import ABC, abstractmethod

class Bank:
	"""
	Abstraction of a bank, capable
	of making transactions and showing
	balance and statements, for a single
	account
	"""
	def __init__(self, initial):
		"""
		:param initial: first value of balance
		when a account is created
		"""
		self.balance = initial
		self.statement = []
	
	def transaction(self, value):
		"""
		:param value: amount considered
		in the transaction, admits negative,
		null and positive inputs
		"""
		if value > 0:
			self.statement.append('cash-in value of ' + str(abs(value)))
		elif value < 0:
			self.statement.append('cash-out value of ' + str(abs(value)))
		else:
			self.statement.append('null transaction')
		self.balance += value

class Order(ABC):
	"""
	Abstract order in Command
	design pattern
	"""
	def __init__(self, bank):
		"""
		Connects to the bank
		"""
		self.bank = bank

	@abstractmethod
	def execute(self):
		"""
		What the order will do
		"""
		pass

class TransactionOrder(Order):
	"""
	A command that realizes a transaction on the bank
	"""
	def __init__(self, bank):
		"""
		Defines the variable that represents
		amount to be transacted
		"""
		self.amount = 0
		super().__init__(bank)

	def execute(self):
		"""
		Calls corresponding function in the bank
		"""
		self.bank.transaction(self.amount)

class BalanceOrder(Order):
	"""
	A command that prints the balance in the bank
	"""
	def execute(self):
		"""
		Prints balance
		"""
		print('balance: ' + str(self.bank.balance))

class StatementOrder(Order):
	"""
	A command that prints the statement in the bank
	"""
	def execute(self):
		"""
		Prints every statement ordered by time the
		statement was created
		"""
		if len(self.bank.statement) == 0:
			print('nothing in current statement')
		else:
			print('current statement:')
			for st in self.bank.statement:
				print(st)

class Agent:
	"""
	Invoker in the Command design pattern
	"""
	def __init__(self):
		"""
		Initializes the queue where all orders
		will be stored until commit
		"""
		self.order_queue = []

	def place_order(self, order):
		"""
		Enqueues an order
		"""
		self.order_queue.append(order)
	
	def commit(self):
		"""
		Executes all orders in the queue,
		cleaning it in the end
		"""
		for order in self.order_queue:
			order.execute()
		self.order_queue *= 0

bank = Bank(100)
transaction_order = TransactionOrder(bank)
balance_order = BalanceOrder(bank)
statement_order = StatementOrder(bank)

agent = Agent()
transaction_order.amount = -50
agent.place_order(transaction_order)
agent.place_order(balance_order)
agent.commit()

transaction_order.amount = -25
agent.place_order(transaction_order)
agent.place_order(balance_order)
agent.commit()

transaction_order.amount = 60
agent.place_order(transaction_order)
agent.place_order(balance_order)
agent.commit()

agent.place_order(statement_order)
agent.commit()

transaction_order.amount = 0
agent.place_order(transaction_order)
agent.place_order(statement_order)
agent.commit()

agent.place_order(balance_order)
agent.commit()

