import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	b,c=new_shape
	a = np.array(a)
	if (b*c) == a.size:
		reshape_matrix = a.reshape(b,c)
		reshape_matrix = reshape_matrix.tolist()
	else:
		reshape_matrix = []
	return reshape_matrix