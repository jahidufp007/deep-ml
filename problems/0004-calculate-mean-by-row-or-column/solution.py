import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = np.array(matrix)
	if mode == "row":
		means = np.mean(means,axis=1)
	else:
		means = np.mean(means,axis=0)
	return means