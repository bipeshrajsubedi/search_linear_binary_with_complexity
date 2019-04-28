import matplotlib.pyplot as plt
from searchAlgorithm import LinearSearch, BinarySearch
import time
import random

def ComplexityLinearSearch():
	x, y = [], []
	for i in range(10000 , 100000, 10000):
		list = [random.randint(0, i) for r in range(i)]
		start_time = time.time()
		LinearSearch(list, list[len(list)-1])
		end_time = time.time()
		diff_time = end_time - start_time
		x.append(i)
		y.append(diff_time)

	plt.plot(x,y)
	plt.show()

def ComplexityBinarySearch():
	x, y = [], []
	for i in range(10000 , 100000, 10000):
		list = [random.randint(0, i) for r in range(i)]
		list.sort()
		start_time = time.time()
		BinarySearch(list, list[len(list)-1])
		end_time = time.time()
		diff_time = end_time - start_time
		x.append(i)
		y.append(diff_time)

	plt.plot(x,y)
	plt.show()

ComplexityLinearSearch()
ComplexityBinarySearch()