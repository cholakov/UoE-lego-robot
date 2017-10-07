
import heapq
from dijkstra import dijkstra, shortest_path

print("Called pathfinder module.")


def goHome():
	print("goHome")

def goTo(arena, origin, target):
	""" 
	Given coordinates, rotate itself to face in that direction.
	Useful for connecting to a satellite.
	:map: matrix of the arena
	:origin: (x,y, thetha) tuple of current pose (in reference to the Arena Coordinate System)
	:target: (x,y) tuple of target position (in reference to the Arena Coordinate System)

	"""

	# check if target is a valid destination (i.e. not 0)
	# Find route from current coordinates to point (x,y). 
	# Go in a straight line unless obstacle on the way. Plan in advance for known obstacles.
	# Plan dynamically for unforseen obstacles. 
	# Djakista search around obstacles


	x = origin[0]
	y = origin[1]

	print("Going from {0} to {1}".format(origin, target))

	if arena[y][x][0] == 0:
		print("ERROR: Sorry, pick another destination. I can't go inside walls.")
		return False

	around = [(-1,-1), 
			(-1,0),
			(-1,1),
			(1,-1),
			(1,0),
			(1,1),
			(0,1),
			(0,-1)]

	graph = {}

	# Create a set of nodes and edges
	# For every node in the ARENA matrix
	for x in range(arena.shape[1]):	# 0 to 29
		for y in range(arena.shape[0]): # 0 to 9
			if arena[y][x][0] == 1: # this constrains node in the graph to represent free space in the real world
				# Find legal surrounding nodes
	   			neighbors = {}
	   			for pos in around:
					a = x + pos[0]
					b = y + pos[1]
					if b >= arena.shape[0] or b < 0:		# goes outside bounds of arena
						continue
					if a >= arena.shape[1] or a < 0: 	# goes outside bounds of arena
						continue	
					if arena[b][a][0] != 1: 			# neighbor node isn't free space
						continue

					name = "x{0}y{1}".format(a,b)
					neighbors[name] = 1
				
				name = "x{0}y{1}".format(x,y)
				graph[name] = neighbors

	start = "x{0}y{1}".format(origin[0],origin[1])
	end = "x{0}y{1}".format(target[0],target[1])

	dist, pred = dijkstra(graph, start=start)

	print("Going from {0} to {1}, the shortest path is:".format(origin, target))
	print(shortest_path(graph, start, end))

	

def explore(arena, origin, objective):
	""" Navigate the space until some objective is achieved, i.e. found reflective tape on the ground. """
	print("explore")

def getUnstuck(arena, origin):
	""" 
	Recovery procedure after getting stuck.
	:return: success after succesfully getting unstuck 

	"""
	print("getUnstuck")




