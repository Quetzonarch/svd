import numpy as np

class Gradient:
	@staticmethod
	def calculate_gradient_highest_sigma(M, v):
		grad = np.zeros((np.size(v, 0), 1))
		for i in range(np.size(v, 0)):
			item = 0
			for j in range(np.size(M, 0)):
				inner_sum = 0
				for k in range(np.size(M, 1)):
					inner_sum += M.item((j, k))*v.item((k, 0))
				inner_sum = M.item((j, i))*inner_sum
				item += inner_sum
			item = item*(-2)
			grad.itemset((i, 0), item)
		return grad

	@staticmethod
	def find_highest_sigma_vector(M):
		#utworzenie losowego wektora jednostkowego
		v = np.random.rand(np.size(M, 1), 1)*2-1
		v = np.divide(v, np.linalg.norm(v))
		a = 0.5
		for i in range(100):
			grad = Gradient.calculate_gradient_highest_sigma(M, v)
			v = np.subtract(v,np.multiply(grad, a))
			v = np.divide(v, np.linalg.norm(v))
		return v

	@staticmethod
	def find_orthogonal_vector(V):
		v = np.random.rand(np.size(V, 0), 1)*2-1
		v = np.divide(v, np.linalg.norm(v))
		a = 0.1
		for i in range(100):
			grad = Gradient.calculate_gradient_highest_sigma(V.T, v)
			grad = grad * (-1.0/np.size(V, 1))
			v = np.subtract(v,np.multiply(grad, a))
			v = np.divide(v, np.linalg.norm(v))
		return v

	@staticmethod
	def calculate_svd(M):
		V = Gradient.find_highest_sigma_vector(M)
		U = M.dot(V)
		S = []
		S.append(np.linalg.norm(U))
		U = U/S[0]
		for i in range(1, min(np.size(M, 0), np.size(M, 1))):
			v = Gradient.find_orthogonal_vector(V)
			u = M.dot(v)
			s = np.linalg.norm(u)
			u = u/s
			V = np.c_[V, v]
			U = np.c_[U, u]
			S.append(s)
		return U, S, V