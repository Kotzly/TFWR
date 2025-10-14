ws = get_world_size()

def walk_direction(n, direction, callback=None, args=None):
	if n < 0:
		direction = {
			East: West,
			West: East,
			South: North,
			North: South
		}[direction]
		n = -n
	for i in range(n):
		if callback:
			if args:
				callback(args)
			else:
				callback()
		move(direction)

def go_to_col_or_row(i, kind="col", callback=None, args=None):
	pos_func = {
		"col": get_pos_x,
		"row": get_pos_y
	}[kind]

	my_pos = pos_func()
	# print("pos", my_pos)
	dright = ((i - my_pos) % ws)
	dleft = ((my_pos - i) % ws)
	n = min(dright, dleft) #* ((dright < dleft) - 2)
	if dright > dleft:
		n = -n
				
	walk_direction(
		n,
		{
			"col": East,
			"row": North
		}[kind],
		callback,
		args
	)
			
def go_to(x, y, callback=None, args=None):
	go_to_col_or_row(x, "col", callback, args)
	go_to_col_or_row(y, "row", callback, args)
				
def dummy():
	print(get_pos_x())

#go_to(1, 1, dummy)
#go_to_col_or_row(7, "col")
# walk_direction(50, South)