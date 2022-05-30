import random, string

class Rabbit:

	def __init__(self, coord, canvas):
		self.damage = 1
		self.tags = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
		canvas.create_rectangle(coord, fill="green", tags=self.tags)

	def __str__(self):
		return 'R'


	def fight(self, oponent):
		return True if self.damage > oponent.damage else False