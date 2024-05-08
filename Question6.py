# Search in row wise and column wise sorted matrix

from typing import List

class Problem:
    def question(self):
        arr = [[10, 20, 30, 40],
            [15, 25, 35, 45],
            [27, 29, 37, 48],
            [32, 33, 39, 50]]
        sol = Solution()
        sol.search_in_sorted_matrix(arr, 4, 4, 29)

class Solution:
    def search_in_sorted_matrix(self, arr: List[List[int]], row: int, col: int, item: int):
        i, j = 0, col - 1
        while i < row and j >= 0:
            if arr[i][j] == item:
                print(f"Found at ({i}, {j})")
                return
            elif arr[i][j] > item:
                j -= 1
            else:
                i += 1
        print("Item not found in matrix")

if __name__ == "__main__":
    sol = Problem()
    sol.question()