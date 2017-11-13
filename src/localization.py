import numpy as np

import math
import time
import pickle
from collections import namedtuple

class Localization():
	def __init__(self):

		# LOAD FROM DISK
		self.poses_np = pickle.load(open("poses_np.np", 'rb'))

		# COPY PARAMETERS
		# THOSE HAVE TO MATCH EXACTLY PARAM IN MAP
		self.RESOLUTION_POS = round(0.1,1)
		self.RESOLUTION_ROT = round(3,1) 
		self.W = 4.25
		self.H = 3.2
		self.OFFSET = 0.01


		# PARAMETERS
		self.SENSORS_VARIANCE = {
			'sonar': 0.1,
			'IR_L' : 0.4,
			'IR_R' : 0.4
		}

		# VARIABLES
		# Further than SENSORS_CUTOFF_STD standard deviations from the mean, 
		# we say the sensor readings are improbable for a given pose
		self.SENSORS_CUTOFF_STD = 0.7

		self.CONFIDENCE_SENSORS = 0.6
		self.CONFIDENCE_ODOMETRY = 0.6

	def _match(self, sensor, reading, lookup_value):
		"""
		Determines if a reading from the sensors matches a value 
		in the lookup table with some probability.
		This is useful to find the exact values of 'x' and 'y' as recorded in the lookup table.
		
		"""

		if reading == None:
			if math.isnan(lookup_value):
				return True
			else:
				return False
		elif sensor == "sonar":
			SIGMA = self.SENSORS_VARIANCE['sonar']
		elif sensor == "IR_L":
			SIGMA = self.SENSORS_VARIANCE['IR_L']
		elif sensor == "IR_R":
			SIGMA = self.SENSORS_VARIANCE['IR_R']

		sigma = 1/SIGMA
		mean = lookup_value
		x = reading
		y = sigma*2.5*(1/(sigma*math.sqrt(2*math.pi))*np.exp( -(1/2*sigma**2)*((x - mean))**2))
		if y > self.SENSORS_CUTOFF_STD:
			return True
		return False

	def _closest(self, number, divider):
		"""
		Returns the closest number to 'number'
		divisible without remainder by 'divider'.
		"""
		
		mod = number % divider        # 28
		
		low = number - mod            # 90
		high = number - mod + divider # 120
		if high - number < number - low:
			return high
		else:
			return low
	
	def _locate_row_in_table(self, x, y, theta):
		largest_y = self.poses_np[0][2]
		
		y_block = (360/self.RESOLUTION_ROT)*(np.ceil(self.W/self.RESOLUTION_POS))*(largest_y-y)/self.RESOLUTION_POS
		x_block = (360/self.RESOLUTION_ROT)*(x-self.OFFSET)/self.RESOLUTION_POS
		theta_block = theta/self.RESOLUTION_ROT
		return int(round(y_block + x_block + theta_block))
	
	def _move_belief(self, prob_sum, motion, measurement):
		"""
		Finds posterior probability, given
			distance traveled in a straight line ('x' and 'y' chnge), OR 
			rotation on the spot.
		Posterior self.poses_np = [prior] X [probability after motion model]
	
		"""
		
		for i in range(len(self.poses_np)): # iterate rows
			if self.poses_np[i][0] == 1: # open space, i.e. not coordinates of an obstacle
				theta = self.poses_np[i][3]
				
				# determine most likely pose where we were before the movement
				delta_x = math.sin((theta + motion.angle) % 360) * motion.distance
				delta_y = math.cos((theta + motion.angle) % 360) * motion.distance
				
				prev_x = self._closest(self.poses_np[i][1] - delta_x, self.RESOLUTION_POS) + self.OFFSET
				prev_y = self._closest(self.poses_np[i][2] - delta_y, self.RESOLUTION_POS) + self.OFFSET
				prev_theta = self._closest((theta - motion.angle) % 360, self.RESOLUTION_ROT)
				
				# unless previous positions is outside the boundaries of the arena
				if prev_x > 0 and prev_y > 0: 
					row_idx = self._locate_row_in_table(prev_x, prev_y, prev_theta)

					# look up the probability of the previous pose
					prev_prob = self.poses_np[row_idx][7]

					# update the probability of the current pose accordingly
					self.poses_np[i][7] = self.CONFIDENCE_ODOMETRY * self.poses_np[i][7] + (1-self.CONFIDENCE_ODOMETRY) * prev_prob
				
				# update running tally
				prob_sum += self.poses_np[i][7]
		return prob_sum
  
	def _sense_belief(self, prob_sum, motion, measurement):
		"""
		Finds posterior = [prior] X [probability after measurement]
		
		"""
		
		for i in range(len(self.poses_np)): # iterate rows
			if self.poses_np[i][0] == 1: # of open space, i.e. not coordinates of an obstacle
				match_all = False
				if self._match('sonar',  measurement.sonar,  self.poses_np[i][4]):
					if self._match('IR_L',  measurement.IR_L,  self.poses_np[i][5]):
						if self._match('IR_R',  measurement.IR_R,  self.poses_np[i][6]):
							match_all = True
				
				self.poses_np[i][7] = (self.poses_np[i][7] * (match_all * self.CONFIDENCE_SENSORS + (1-match_all) * (1.0-self.CONFIDENCE_SENSORS)))
				prob_sum += self.poses_np[i][7]
		return prob_sum
		
	def update(self, motion, measurement):
		"""
		self.poses_np    :: a lookup table of possible poses and sensor readings. Columns: open, x, y, theta, sonar, IR_L, IR_R
		measurement :: a tuple of readings from (sonar, IR_L, IR_R).
		
		"""
		t1 = time.time()
		prob_sum = 0
		prob_sum += self._move_belief(prob_sum, motion, measurement)
		prob_sum += self._sense_belief(prob_sum, motion, measurement)
	
		# normalize--> total probability theory
		self.poses_np[:,7] = self.poses_np[:,7] / prob_sum

		t2 = time.time()
		print("Recomputed localization in " + str(t2-t1) + " seconds.")

	def reset(self):
		""" 
		Takes all rows where 0-indexed column 1 one,
		and change 7-indexed column to the prior probability.
		
		"""

		prob = 1.0 / len(self.poses_np[:,0])
		self.poses_np[self.poses_np[:, 0] == 1, 7] = prob


# Measurement = namedtuple('Measurement', ['sonar', 'IR_L', 'IR_R'])
# Motion = namedtuple('Motion', ['distance', 'angle'])
# Pose = namedtuple("Pose", ['x', 'y', 'theta'])

# measurements = [Measurement(0.6, 0.2, 0.3),
# #                 Measurement(0.5, 0.2, 0.3),
# #                 Measurement(0.2, 0.2, 0.3),
# #                 Measurement(0.2, 0.2, 0.3),
# #                 Measurement(0.8, 0.15, None),
# #                 Measurement(0.7, 0.15, None),
# #                 Measurement(0.6, 0.15, None),
# 			   ]

# motions      = [Motion(0.1, 0),
# #                 Motion(0.1, 0),
# #                 Motion(0.1, 0),
# #                 Motion(0.2, 0),
# #                 Motion(0.0, 90),
# #                 Motion(0.1, 90),
# #                 Motion(0.1, 90),
# 			   ]


# localize = Localize()
# localize.reset()

# for i in range(len(measurements)):
# 	localize.update(motions[i], measurements[i])