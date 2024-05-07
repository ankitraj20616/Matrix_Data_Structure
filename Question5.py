# Print Matrix through spiral transversal
from typing import List

class Problem:
    def question(self):
        arr = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]
        sol = Solution()
        sol.spiral_traversal(arr, 4, 4)

class Solution:
    def spiral_traversal(self, arr: List[List[int]], row: int, col: int)-> None:
        top, bottom, left, right = 0, row - 1, 0, col - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                print(arr[top][i], end=" ")
            top += 1
            for i in range(top, bottom + 1):
                print(arr[i][right], end=" ")
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    print(arr[bottom][i], end=" ")
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    print(arr[i][left], end=" ")
                left += 1


if __name__ == "__main__":
    sol = Problem()
    sol.question()