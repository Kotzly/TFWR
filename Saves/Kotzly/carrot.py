def plant_carrot():
	if get_ground_type() == Grounds.Grassland:
		till()
	if get_entity_type() != Entities.Carrot and can_harvest():
		harvest()
	elif get_entity_type == Entities.Carrot:
		return False
	plant(Entities.Carrot)
	return True
	