import random, string

class Wolf:

	def __init__(self, coord, canvas):
		self.damage = 2
		self.tags = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
		canvas.create_rectangle(coord, fill="blue", tags=self.tags)

	def __str__(self):
		return 'W'


	def fight(self, oponent):
		return True if self.damage > oponent.damage else False