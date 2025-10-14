from cactus import plant_cactus, move_cacti
from moving import go_to
from positions import all_pos
clear()
for px, py in all_pos((3, 4), (3, 9)):
	go_to(px, py)
	plant_cactus()