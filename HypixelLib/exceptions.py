class APIError(Exception):
	def __init__(self, error):
		self.error = error

class InvalidAPIKeyError(Exception):
	def __init__(self, error):
		self.error = error


class InvalidPlayerNameError(Exception):
	pass

class NoInputError(Exception):
	pass