class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.matrix = matrix.copy()
        for i in range(row):
            for j in range(1,col):
                self.matrix[i][j] = self.matrix[i][j-1] + self.matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1,row2 + 1):
            if col1 is 0:
                sum += self.matrix[i][col2]
            else:
                sum = sum + self.matrix[i][col2] - self.matrix[i][col1-1]
        return sum




        """
        [[3, 0, 1, 4, 2],
         [5, 6, 3, 2, 1],
         [1, 2, 0, 1, 5],
         [4, 1, 0, 1, 7],
         [1, 0, 3, 0, 5]
         ],

         [3, 3, 4,  8,  10],
         [5, 11, 14, 16, 17],
         [1, 3,  3,   4,  9],
         [4, 5,  5,   6,  13],
         [1, 1,  4,   4,   9]
         ]
        """


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# come there today
# param_1 = obj.sumRegion(row1,col1,row2,col2)