from moving import go_to
from positions import get_map
from create_maze import create_maze

global args
args  = None

def solve(d0=0, turn_right=True):
	d = d0
	while get_entity_type() != Entities.Treasure:
		new_d = (d + 1) % 4
		if can_move(dirs[new_d]):
			d = new_d
			move(dirs[d])
		else:
			dir = dirs[d]
			if not move(dir):
				d = (d + 2) % 4
				while not can_move(dirs[d]):
					d = (d + 1) % 4	
	harvest()

dirs = [North, East, South, West]

def solve(d0=0, confusion=0, turn_right=True):
						
	d = d0
	r1, r2 = 1, -1
	if not turn_right:
		r1, r2 = r2, r1
	
	while get_entity_type() == Entities.Hedge:
		new_d = (d + r1) % 4
		if random() < confusion:
			r1, r2 = r2, r1
		if move(dirs[new_d]):
			d = new_d
		else:
			while not move(dirs[d]):
				d = (d + r2) % 4
	
	if get_entity_type() == Entities.Treasure:
		harvest()
		quick_print("Solved by", args)
						
def solve_dir(d0, confusion=0, turn_right=True):
			
	d = d0
	r1, r2 = 1, -1	
	if not turn_right:
		r1, r2 = -1, 1
	while get_entity_type() == Entities.Hedge:
		new_d = (d + r1) % 4
		txy = measure()
		if not txy:
			return
		tx, ty = txy
		
		if random() < confusion:
			if random() < 0.5:
				new_d = 1
				if tx < get_pos_x():
					new_d = 3
			else:
				new_d = 0
				if ty < get_pos_y():
					new_d = 2
							
		if move(dirs[new_d]):
			d = new_d
		else:
			while not move(dirs[d]):
				d = (d + r2) % 4
	
	if get_entity_type() == Entities.Treasure:
		harvest()	
		quick_print("Solved by crazy drone:", args)

def job_solve_dir():
	
	global args
	d0, confusion, turn_right = 0, 0, True
	if args:
		if len(args) == 1:
			d0 = args
		elif len(args) == 2:
			d0, confusion,  = args
		elif len(args) == 3:
			d0, confusion, turn_right = args
	solve_dir(d0, confusion, turn_right)
	
def job_solve():
	
	global args
	d0, confusion, turn_right = 0, 0, True
	if args:
		if len(args) == 1:
			d0 = args
		elif len(args) == 2:
			d0, confusion,  = args
		elif len(args) == 3:
			d0, confusion, turn_right = args
	solve(d0, confusion, turn_right)
	
def print_ent():
	print(get_entity_type())
		
if __name__ == "__main__":
	args = None
	while True:

		create_maze(88)
		#spawn_drone(print_ent)
		
#		solve()
#		continue
		drones = list()
		
		turn_right = True
		
		args = (0, 0, True)
		drones.append(spawn_drone(job_solve))
		args = (0, 0, False)
		drones.append(spawn_drone(job_solve))
				
		for i in range((max_drones() - 2) // 2):
			args = [i % 4, i * 0.005, turn_right]
			drones.append(
				spawn_drone(job_solve_dir)
			)
			drones.append(
				spawn_drone(job_solve)
			)
			turn_right = not turn_right
				
		solve_dir(0, 0.01, True)
		for drone in drones:
			if not (drone == None):
				wait_for(drone)