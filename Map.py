import random


class Map:

	def __init__(self, row, col, animals, canvas):
		self.row = row
		self.col = col
		self.animals = animals
		self.canvas = canvas
		self.map_object = list()


	def init_map(self):
		for i in range(self.row+1):
			row = list()
			for j in range(self.col+1):
				width = 10
				distance = 1+width
				coord = (distance*i, distance*j, distance*i+width, distance*j+width,)
				row.append(random.choice(self.animals)(coord=coord, canvas=self.canvas))
			self.map_object.append(row)


	def get_random_animal(self):
		x = random.randint(0, self.row)
		y = random.randint(0, self.col)
		return {'animal': self.map_object[x][y], 'row': x, 'col': y}


	def view_map(self):
		result = ""
		for row in self.map_object:
			row_res = ""
			for item in row:
				row_res += str(item)
			result += row_res+'\n'
		return result


	def set_area_live(self, animal):
		
		def propagation(x, y):
			range_start_x = x-1 if x != 0 else 0
			range_finish_x = x+1 if x == self.row else x+2
			for neighbor_x in range(range_start_x, range_finish_x):
				range_start_y = y-1 if y != 0 else 0
				range_finish_y = y+1 if y == self.col else y+2
				for neighbor_y in range(range_start_y, range_finish_y):
					if self.map_object[neighbor_x][neighbor_y] == '*' or self.map_object[neighbor_x][neighbor_y] == '@':
						continue
					if neighbor_x == animal['row'] and neighbor_y == animal['col']:
						self.map_object[neighbor_x][neighbor_y] = '@'
						continue
					if animal['animal'].fight(self.map_object[neighbor_x][neighbor_y]):
						print(self.map_object[neighbor_x][neighbor_y].tags)
						self.canvas.delete(self.map_object[neighbor_x][neighbor_y].tags)
						self.map_object[neighbor_x][neighbor_y] = '*'
						propagation(neighbor_x, neighbor_y)


		propagation(animal['row'], animal['col'])
