import numpy as np
import pickle

poses = pickle.load(open("poses.df", 'rb'))

poses_np = np.array(poses.values)
pickle.dump(poses_np, open("poses_np.np", 'wb'))