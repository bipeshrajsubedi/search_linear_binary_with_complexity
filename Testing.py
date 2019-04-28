import unittest
from searchAlgorithm import LinearSearch ,BinarySearch

class TestSearchAlgorithms(unittest.TestCase):

	def test_linearSearch(self):
		list = [6,5,1,4,10,12,3,0]
		self.assertEqual(LinearSearch(list, 1), 2)

	def test_BinarySearch(self):
		list = [1,2,3,4,5,6,7,8]
		self.assertEqual(BinarySearch(list, 5), 4)


if __name__ == "__main__":
	unittest.main()