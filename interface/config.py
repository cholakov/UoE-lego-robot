import numpy as np
# Define settins here

DEST = []
OBJECTIVE = []

# This is some massive matrix
# Define free areas
arena = np.array([[[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
				  [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
				  [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0], [1], [1], [1], [1], [1], [1], [1], [0], [0], [1], [1], [1], [1], [1], [1], [1], [1]],
				  [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0], [0], [0], [1], [1], [1], [1], [1], [1], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
				  [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0], [0], [0], [0], [1], [1], [1], [1], [1], [0], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
				  [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0], [0], [0], [0], [0], [1], [1], [1], [1], [0], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
				  [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0], [0], [0], [1], [1], [1], [1], [1], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
				  [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0], [1], [1], [1], [1], [0], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
				  [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
				  [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]])
# ARENA.shape
# # Give each pixel an x, y position
# ARENA = np.expand_dims(ARENA, 2)
# # x
# for i in range(ARENA.shape[0]):
# 	for j in range(ARENA.shape[1]):
# 		ARENA[i][j] = i

# print(ARENA)
# # y
# for j in range(ARENA.shape[1]):
# 	ARENA[:,j,:] = j