class Subscriber():
	"""docstring for Subscriber"""
	def __init__(self, name,email):
		super(Subscriber, self).__init__()
		self.name = name
		self.email = email

	def get_subscriber(self):
		sub = {}
		sub[" name"] = self.name
		sub["email"] = self.email
		return sub