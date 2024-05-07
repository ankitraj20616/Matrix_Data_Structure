# Transpose of a matrix

from typing import List
class Problem:
    def question(self):
        arr = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]
        sol = Solution()
        sol.find_transpose_2(arr)
        for row in arr:
            print(row)

class Solution:
    def find_transpose_1(self, arr: List[List[int]], size: int)-> None:
        temp = [[0] * size for _ in range(size)]
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                temp[i][j] = arr[j][i]
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j] = temp[i][j]
    
    def find_transpose_2(self, arr: List[List[int]])-> None:
        for i in range(len(arr)):
            for j in range(i+1, len(arr[i])):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


if __name__ == "__main__":
    sol = Problem()
    sol.question()