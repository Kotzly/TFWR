from positions import all_pos
from carrot import plant_carrot
from pumpkin import plant_pumpkin
from wood import plant_bush, plant_tree
from grass import plant_grass
from simple_moving import go_to


def to_grass():
	if get_ground_type() != Grounds.Grassland:
		till()


plant_fn_dict = {
	Entities.Bush: plant_bush,
	Entities.Tree: plant_tree,
	Entities.Carrot: plant_carrot,
	Entities.Grass: plant_grass
}

while True:
	to_plant = all_pos()
	planted = list()
	companions = list()
	
	comp = None
	ent = Entities.Grass
	
	
	
	while len(to_plant) > 0:
		comp = to_plant[0]
		go_to(comp[0], comp[1])
		plant_fn_dict[ent]()
	
		companions.append(to_plant.pop(0))
	
		ent, comp = get_companion()
	
		if not (comp in companions):
			to_plant.remove(comp)
			to_plant.insert(0, comp)
	
		
	for pos in companions:
		go_to(pos[0], pos[1])
		harvest()
					