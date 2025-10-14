from moving import go_to
from wood import plant_bush

def create_maze(n=44):
	harvest()
	go_to(1, 1)
	plant_bush()
	while not can_harvest():
		use_item(Items.Fertilizer)
	
	use_item(Items.Weird_Substance, n)
	
	if get_entity_type() == Entities.Treasure:
		harvest()