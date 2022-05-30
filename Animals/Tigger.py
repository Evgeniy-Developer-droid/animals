import random, string

class Tigger:

	def __init__(self, coord, canvas):
		self.damage = 3
		self.tags = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
		canvas.create_rectangle(coord, fill="red", tags=self.tags)


	def __str__(self):
		return 'T'
		

	def fight(self, oponent):
		return True if self.damage > oponent.damage else False