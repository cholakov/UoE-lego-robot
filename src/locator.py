# class Locator:
# 	def __init__(self):
# 		print("Localization in progress.")
# 		self.x = None
# 		self.y = None
# 		self.theta = None

# 	def set(self, x, y, theta):
# 		self.x = x
# 		self.y = y
# 		self.theta = theta

# 	def pose(self):
# 		"""
# 		:return: (x,y,theta) in relation to the Arena Coordinate System
# 		"""

# 		# obviously very dummy at this point
# 		return((self.x, self.y, self.theta))

# 2D localization for a small arena

from numpy import * # used in show(p) func

def localize(arena, measurements, motions, sensor_right, move_right):
	# initializes p to a uniform distribution over a grid of the same dimensions as arena
	[row, col]=shape(arena)
	p0 = 1.0 / float(row) / float(col) # average a scalar number, uniform distribution
	p = p0*ones((row, col))          
	q = zeros((row, col))

	for step in range(len(measurements)):
		U = motions[step]
		for i in range(len(p)): # iterate rows
			xx=[]
			for j in range(len(p[0])): # iterate columns
				# multiply surrounding squares by 0.8 (unless on the edge of arena), and the rest by 0.2
				# i-U[0] -1/+1 square UP or DOWN, 
				# j-U[1] -1/+1 square RIGHT or LEFT
				# % len() evaluates to 0 on the edges of the arena
				xx.append(move_right * p[(i-U[0]) % len(p)][(j-U[1]) % len(p[0])] + (1.0-move_right)*p[i][j] )
			q[i]=xx

		p_sum=sum(p)
		p = q/p_sum

		# print('\n Probability after motion, @step', step+1)
		# show(p)

		sonar = 2.9
		std = 0.1

		
		# posterior = [prior] X [probability after measurement]
		for i in range(len(p)): # iterate rows
			for j in range(len(p[0])): # iterate columns               
				match = (measurements[step] == arena[i][j]) # True or False
				# multiply squares where measurement is True by 0.8, and the rest by 0.2
				p[i][j] = (p[i][j] * (match * sensor_right + (1-match) * (1.0-sensor_right)))	
				#print step, U, i, j
		# p_sum=sum(p)
		p = p/p_sum  # normalize--> total probability theory
		print('p sum', p_sum)

		print('Probability after measurement')
		show(p)
	return p

def show(p):
	print(around(p,decimals=3))
	
	
#############################################################
# Given sensor_right = 0.8, move_right = 0.8, 
# Final results:
#[[ 0.036  0.085  0.047  0.083  0.015]
# [ 0.014  0.038  0.114  0.011  0.014]
# [ 0.007  0.045  0.327  0.017  0.009]
# [ 0.016  0.021  0.042  0.043  0.016]]

arena=[['wall','none','none','none','wall'],
	   ['wall','wall','none','none','none'],
	   ['wall','wall','none','none','none'],
	   ['wall','wall','wall','wall','wall']]

# len(arena)=4, shape(arena)=(4, 5), it is a 4 row, 5 column arena.
# note that in arena[x][y], x is the index for row, and y is the index for column,
# initial position is arena[0][0], at top left corner
# so motions are
# [0,1] -  move right
# [0,-1] - move left
# [-1,0] - move  up
# [1,0] -  move down

measurements = ['wall','none','wall','wall','none']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
p = localize(arena, measurements, motions, sensor_right = 0.8, move_right = 0.8)
# print('\n Final results:')
# show(p) # displays your answer

# Note: numerical accuracy matters, if you don't normalized after move, then p value is so small that it will
# be truncated off, then sense will not be accurate.