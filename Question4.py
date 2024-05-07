# Rotate the matrix by 90*

from typing import List
from Question3 import Solution as transpose
class Problem:
    def question(self):
        arr = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]
        sol = Solution()
        sol.rotate_matrix_acutely_2(arr)
        for row in arr:
            print(row)

class Solution:
    def rotate_matrix_acutely_1(self, arr: List[List[int]])-> None:
        temp = [[0] * len(arr) for _ in range(len(arr))]
        for i in range(len(arr)):
            for j in range(len(arr)):
                temp[len(arr) - j - 1][i] = arr[i][j]

        for i in range(len(arr)):
            for j in range(len(arr)):
                arr[i][j] = temp[i][j]
    
    def reverse_matrix(self, arr: List[List[int]])-> None:
        for i in range(len(arr)//2):
            for j in range(len(arr[i])):
                arr[i][j], arr[len(arr) - i - 1][j] = arr[len(arr) - i - 1][j], arr[i][j]
    
    def rotate_matrix_acutely_2(self, arr: List[List[int]])-> None:
        transpose.find_transpose_2(self=Solution, arr= arr)
        self.reverse_matrix(arr)



if __name__ == "__main__":
    sol = Problem()
    sol.question()