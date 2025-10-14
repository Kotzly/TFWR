from positions import all_pos
from moving import go_to


def plant_wood():
	px, py = get_pos_x(), get_pos_y()
	if get_ground_type() != Grounds.Grassland:
		till()
	if get_water() < 0.3:
		use_item(Items.Water)
	if (px + py) % 2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)

def plant_bush():
	if get_ground_type() != Grounds.Grassland:
		till()
	plant(Entities.Bush)
	
def plant_tree():
	if get_ground_type() != Grounds.Grassland:
		till()
	if get_water() < 0.3:
		use_item(Items.Water)
	plant(Entities.Tree)
		
	
def wood_season(seasons=1, xbounds=None, ybounds=None):
	pos_list = all_pos(xbounds, ybounds)
	planted = list()
	for season in range(seasons):
		for px, py in pos_list:
			go_to(px, py)
			if can_harvest() and get_entity_type() in (Entities.Bush, Entities.Tree):
				harvest()

			plant_wood()
			planted.append((px, py))
		while len(planted) > 0:
			px, py = planted[0]
			go_to(px, py)
			if can_harvest():
				harvest()
				planted.pop(0)
				if season < seasons:
					plant_wood()
			else:
				planted.append(planted.pop(0))
						

if __name__ == "__main__":
	while True:
		wood_season(2)