
def all_pos(xbounds=None, ybounds=None):
	ws = get_world_size()
	if not xbounds:
		xbounds = (0, ws)
	if not ybounds:
		ybounds = (0, ws)

	post_list = []
	for i in range(xbounds[0], xbounds[1]):
		for j in range(ybounds[0], ybounds[1]):
			post_list.append((i, j))
	return post_list
	
def get_map(x, y, x0=0, y0=0, default=None):
	map = dict()
	for i in range(x0, x0 + x):
		map[i] = dict()
		for j in range(y0, y0 + y):
			map[i][j] = default
	return map