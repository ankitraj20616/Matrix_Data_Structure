# Print Matrix in Snake pattern

from typing import List

class Problem:
    def question(self):
        arr = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]
        sol = Solution()
        sol.print_snake_pattern(arr)

class Solution:
    def print_snake_pattern(self, arr: List[List[int]])-> None:
        for i in range(len(arr)):
            if i % 2 == 0:
                for j in range(len(arr[i])):
                    print(arr[i][j], end=" ")
            else:
                for j in range(len(arr[i]) - 1, -1, -1):
                    print(arr[i][j], end=" ")

if __name__ == "__main__":
    sol = Problem()
    sol.question()