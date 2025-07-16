class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.sums = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                upper_sum = self.sums[i - 1][j]
                side_sum = self.sums[i][j - 1]
                intersection = self.sums[i - 1][j - 1]
                value = matrix[i - 1][j - 1]
                self.sums[i][j] = value + upper_sum + side_sum - intersection


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.sums[row2 + 1][col2 + 1]
        upper = self.sums[row1][col2 + 1]
        side = self.sums[row2 + 1][col1]
        intersection = self.sums[row1][col1]

        return total - upper - side + intersection



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)