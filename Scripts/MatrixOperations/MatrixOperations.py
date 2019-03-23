
class MatrixOperations(object):
    def __init__(self, matrix):
        self.matrix = matrix
        
    def RowSum(self):
        return [
                list(rowSum) for rowSum in 
                zip([rowName[0] for rowName in self.matrix[1:]],[sum(row[1:]) for row in self.matrix[1:]])
               ]
    
    def ColumnSum(self):
        return [
                 list(colSum) for colSum in
                 zip(self.matrix[0][1:],
                     [sum([row[col] for row in self.matrix[1:]]) for col in range(1,len(self.matrix[0]))]
                     )
                 ]


x = MatrixOperations(
    [["Person/Stock","Product1", "Product2","Product3"],
     ["John",100, 20, 30],
     ["Keith",20, 40, 10],
     ["Russel",20, 60, 20]])

print(x.RowSum())

print(x.ColumnSum())