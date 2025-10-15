from positions import all_pos
from carrot import plant_carrot
from pumpkin import plant_pumpkin
from wood import plant_bush, plant_tree
from grass import plant_grass
from simple_moving import go_to

MAX_CACTUS_SIZE = 9

to_plant = all_pos((0, 1), (0, 22))

def plant_cactus():
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Cactus:
		harvest()
	plant(Entities.Cactus)

def move_cacti(start, finish):
	if start == finish:
		return
	sx, sy = start
	fx, fy = finish
	go_to(sx, sy)
	d = fy - sy

	if sy < fy:
		direction = North
	else:
		direction = South
		d = -d

	for i in range(d):
		swap(direction)
		move(direction)
		
			
			

def sort(col, y1, y2=None):
		
	if not y2:
		y2 = get_world_size()
	go_to(col, y2 - 1)
	total_count = 0
	size = MAX_CACTUS_SIZE
	while size > 0:
		while get_pos_y() > y1:
			move(South)
			if measure() == size:
				move_cacti((col, get_pos_y()), (0, y2 - total_count - 1))
				total_count += 1
		go_to(col, y2 - total_count)
		size -= 1
			
	
	

if __name__ == "__main__":
	while True:
		for x, y in to_plant:
			go_to(x, y)
			harvest()
			use_item(Items.Water)
			plant_cactus()
			if random() < 0.1:
				use_item(Items.Weird_Substance)
		sort(0, 0, get_world_size())
	