from positions import all_pos
# time_passed = get_time
time = 0
start_time = get_time()

def plant_sunflower():
	if get_ground_type() == Grounds.Grassland:
		till()
	if get_entity_type() != Entities.Sunflower and can_harvest():
		harvest()
	elif get_entity_type == Entities.Sunflower:
		return False

	plant(Entities.Sunflower)
	return True


from moving import go_to
# 0 unkown
# 1 planted growing
# 2 planted grown
# 3 planted rotten		

def get_size_dict():
	size_dict = dict() 
	for i in range(7, 15 + 1):
		size_dict[i] = list()
	return size_dict

def sunflower_season(xbounds=None, ybounds=None):
	planted = [all_pos(xbounds, ybounds), []]

	size_dict = get_size_dict()

	while len(planted[0]) > 0:
		(posx, posy) = planted[0].pop()
		go_to(posx, posy)
		plant_sunflower()
		planted[1].append((posx, posy))


	ws = get_world_size()
	go_to(0, 0)	
	while not can_harvest():
		pass
	size_dict[measure()].append((0, 0))
	x, y = 0, 0
	while (x, y) != (ws-1, ws-1):
		move(North)
		x, y = get_pos_x(), get_pos_y()
		while not can_harvest():
			pass
		size = measure()
		size_dict[size].append((x, y))
		if get_pos_y() == (ws - 1):
			move(East)
			
	
	
	for size in range(15, 7 - 1, -1):
		l = size_dict[size]

		while len(l) > 0:
			px, py = l[0]
			def callback():
				xx, yy = (get_pos_x(), get_pos_y())
				if (xx, yy) in l:
					l.remove((xx, yy))
					harvest()
			go_to(px, py, callback)
			while not can_harvest() and get_entity_type() == Entities.Sunflower:
				pass
			l.remove((px, py))
			harvest()
			
				
			
	print("Flower time!!!")
	
if __name__ == "__main__":
	while True:
		sunflower_season()