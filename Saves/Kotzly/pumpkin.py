from positions import all_pos
# time_passed = get_time
time = 0
start_time = get_time()

def plant_pumpkin():
	if get_ground_type() == Grounds.Grassland:
		till()
	if get_entity_type() != Entities.Pumpkin and can_harvest():
		harvest()
	elif get_entity_type == Entities.Pumpkin:
		return False
	plant(Entities.Pumpkin)
	return True

def get_map():
	x = get_world_size()
	world_map = []
	for i in range(x):
		world_map.append([])
		for j in range(x):
			world_map[i].append(0)
	return world_map

	
def check():
	status = 0
	if get_entity_type() == Entities.Dead_Pumpkin:
		status = 3
	elif get_entity_type() == Entities.Pumpkin:
		if can_harvest():
			status = 2
		else:
			status = 1
	
	return status






from moving import go_to

# 0 unkown
# 1 planted growing
# 2 planted grown
# 3 planted rotten		


def pumpkin_season(xbounds=None, ybounds=None):
	planted = [all_pos(xbounds, ybounds), [], [], []]
		
	def callback():
		status = check()
		x, y = get_pos_x(), get_pos_y()
		if status == 2 and (x, y) in planted[1]:
			planted[1].remove((x, y))

	while len(planted[0]) > 0:
		(posx, posy) = planted[0].pop()
		go_to(posx, posy, callback)
		plant_pumpkin()
		planted[1].append((posx, posy))


	while len(planted[1]) > 0:
		(posx, posy) = planted[1][0]
		go_to(posx, posy, callback)
		status = check()
		if status in (0, 3):
			plant_pumpkin()
			if get_water() < 0.0:
				use_item(Items.Water)
			planted[1].append(planted[1].pop(0))
		elif status == 1:
			planted[1].append(planted[1].pop(0))
			continue
		elif status == 2:
			if (posx, posy) == planted[1][0]:
				planted[1].remove((posx, posy))
			continue
			
	print("Pumpkin time!!!")
	harvest()
	
if __name__ == "__main__":
	while True:
		pumpkin_season()