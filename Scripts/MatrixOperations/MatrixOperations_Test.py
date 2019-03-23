import unittest

from MatrixOperations import MatrixOperations

class MatrixOperations_TestClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.x = MatrixOperations(
                     [["Person/Stock","Product1", "Product2","Product3"],
                     ["John",100, 20, 30],
                     ["Keith",20, 40, 10],
                     ["Russel",20, 60, 20]])

    def test_ColumnSum(self):
        val = self.x.ColumnSum()
        self.assertListEqual(val,[["Product1",140], ["Product2",120],["Product3",60]])

    def test_RowSum(self):
        val = self.x.RowSum()
        self.assertListEqual(val,[["John",150], ["Keith",70],["Russel",100]])

if __name__ == '__main__':
    unittest.main()
