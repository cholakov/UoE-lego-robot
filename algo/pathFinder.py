
import heapq
from dijkstra import dijkstra, shortest_path
from algo.driver import Driver


print("Called pathfinder module.")

class pathFinder():
	def __init__(self, IO, origin=None, target=None):
		"""
		Has information of current location using abstract representation.
		Sends abstract commands to Driver, which will convert them to meters.
		"""
		self.origin = origin
		self.target = target
		self.IO = IO
		self.driver = Driver(self.IO)

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

						neighbors[(a,b)] = 1

					graph[(x,y)] = neighbors

		dist, pred = dijkstra(graph, start=origin)

		print("Going from {0} to {1}, the shortest path is:".format(origin, target))
		print(shortest_path(graph, origin, target))


	def explore(arena, objective=None):
		""" Navigate the space until some objective is achieved, i.e. found reflective tape on the ground. """
		print("Exploring")

		self.driver.goTo((1,1,0))




