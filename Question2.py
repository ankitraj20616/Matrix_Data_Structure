# Print boundary elements in matrix

from typing import List

class Problem:
    def question(self):
        arr1 = [[1, 2, 3, 4]]
        arr2 = [[1], [2], [3], [4]]
        arr3 = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]
        sol = Solution()
        sol.print_boundary_elements(arr1, 1, 4)
        print()
        sol.print_boundary_elements(arr2, 4, 1)
        print()
        sol.print_boundary_elements(arr3, 4, 4)

class Solution:
    def print_boundary_elements(self, arr: List[List[int]], row: int, col: int)-> None:
        if row == 1:
            for i in range(col):
                print(arr[row - 1][i], end=" ")
            return
        elif col == 1:
            for i in range(row):
                print(arr[i][col - 1], end=" ")
            return
        else:
            for i in range(col):
                print(arr[0][i], end=" ")
            for i in range(1, row):
                print(arr[i][col - 1], end=" ")
            for i in range(col - 2, -1, -1):
                print(arr[row - 1][i], end=" ")
            for i in range(row - 2, 0,  -1):
                print(arr[i][0], end=" ")

if __name__ == "__main__":
    sol = Problem()
    sol.question()