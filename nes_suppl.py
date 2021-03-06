import numpy as np


actions_l = np.concatenate((np.linspace(-5.0, -2.0, num=4), np.linspace(-1.5, -1.0, num=2), 
	np.linspace(-0.8, 0.8, num=9), np.linspace(1.0, 1.5, num=2), np.linspace(2.0, 5.0, num=4)))

ACTIONS = np.array([(i, j) for i in actions_l for j in actions_l])

# ACTIONS = np.array([(i / 10, j / 10) for i in range(-50, 51, 25) for j in range(-50, 51, 25)])

def basis_functions(obs):
	obs_1, obs_2, obs_3, obs_4, obs_5, obs_6, obs_7, obs_8 = [*obs]
	basis_f = np.array([obs_1, obs_2, obs_3, obs_4, obs_5, obs_6, obs_7, obs_8, obs_1 * obs_2, obs_1 * obs_3, obs_1 * obs_4,
					obs_1 * obs_5, obs_1 * obs_6, obs_1 * obs_7, obs_1 * obs_8, obs_2 * obs_3, obs_2 * obs_4, obs_2 * obs_5, 
					obs_2 * obs_6, obs_2 * obs_7, obs_2 * obs_8, obs_3 * obs_4, obs_3 * obs_5, obs_3 * obs_6, obs_3 * obs_7,
					obs_3 * obs_8, obs_4 * obs_5, obs_4 * obs_6, obs_4 * obs_7, obs_4 * obs_8, obs_5 * obs_6, obs_5 * obs_7,
					obs_5 * obs_8, obs_6 * obs_7, obs_6 * obs_8, obs_7 * obs_8, obs_1 * obs_2 * obs_3 * obs_7, 
					obs_4 * obs_5 * obs_6 * obs_8])
	return basis_f.reshape((basis_f.size, 1))


ACTIONS_S = np.array([-2.0, -1.8, -1.5, -1.2, -1.0, -0.8, -0.5, -0.25, 0.0, 0.25, 0.5, 0.8, 1.0, 1.2, 1.5, 1.8, 2.0])


def basis_functions_s(obs):
	obs_1, obs_2, obs_3 = [*obs]
	basis_f = np.array([obs_1, obs_2, obs_3, obs_1 ** 2, obs_2 ** 2, obs_3 ** 3, 
						obs_1 * obs_2, obs_1 * obs_3, obs_2 * obs_3])
	return basis_f.reshape((basis_f.size, 1))



