
from Animals.Tigger import Tigger
from Animals.Wolf import Wolf
from Animals.Rabbit import Rabbit
from Map import Map
import sys
import tkinter

sys.setrecursionlimit(30*70)

root = tkinter.Tk()

C = tkinter.Canvas(root, bg="white", height=1000, width=1000)
map_obj = Map(row=30, col=30, animals=[Tigger, Wolf, Rabbit], canvas=C)

map_obj.init_map()

# print(map_obj.view_map())
animal = map_obj.get_random_animal()
# print(animal)
map_obj.set_area_live(animal)
# print(map_obj.view_map())




C.pack()
root.mainloop()