ws = get_world_size()

def walk_direction(n, direction):
	if n < 0:
		direction = {
			East: West,
			West: East,
			South: North,
			North: South
		}[direction]
		n = -n
	for i in range(n):
		move(direction)

def go_to_col(i):

	my_pos = get_pos_x()
	# print("pos", my_pos)
	dright = ((i - my_pos) % ws)
	dleft = ((my_pos - i) % ws)
	n = min(dright, dleft) #* ((dright < dleft) - 2)
	if dright > dleft:
		n = -n
				
	walk_direction(
		n,
		East
	)
	

def go_to_row(i):

	my_pos = get_pos_y()
	# print("pos", my_pos)
	dright = ((i - my_pos) % ws)
	dleft = ((my_pos - i) % ws)
	n = min(dright, dleft) #* ((dright < dleft) - 2)
	if dright > dleft:
		n = -n
				
	walk_direction(
		n,
		North
	)
			
def go_to(x, y):
	go_to_col(x)
	go_to_row(y)
	
				
def dummy():
	print(get_pos_x())

#go_to(1, 1, dummy)
#go_to_col_or_row(7, "col")
# walk_direction(50, South)