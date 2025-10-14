from moving import go_to
from positions import get_map

directions = [North, East, South, West]

map = get_map(6, 6)
b1, b2 = 0, 1
while get_entity_type() != Entities.Treasure:
	if not can_move(directions[b1]) and can_move(directions[b2]):
		move(directions[b2])
	elif can_move(directions[b2]) and not can_move(directions[b1]):
		move(directions[b1])
	else:
		b2 = (b2 + 1) % 4
		b1 = (b1 + 1) % 4
		move(directions[b2])
						
if get_entity_type() != Entities.Treasure:
	harvest()