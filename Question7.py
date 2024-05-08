# Find median in row wise sorted matrix

from typing import List

class Problem:
    def question(self)-> None:
        arr = [[2, 4, 6, 8, 10],
               [1, 3, 5, 7, 9],
               [100, 200, 400, 500, 800]]
        sol = Solution()
        print(f"Median of matrix is {sol.find_median_2(arr, 3, 5)}")
        

class Solution:
    def find_median_1(self, arr: List[List[int]], row: int, col: int)-> int:
        temp = [0] * (row * col)
        index = 0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                temp[index] = arr[i][j]
                index += 1
        temp = sorted(temp)
        return temp[len(temp)//2]
    
    def count_lesser_elements(self, arr: List[List[int]], row: int, col: int, x: int)-> int:
        count = 0
        for i in range(row):
            low = 0
            high = col - 1
            while low <= high:
                mid = low + ((high - low)//2)
                if arr[i][mid] < x:
                    count += (mid - low + 1)
                    low = mid + 1
                else:
                    high = mid - 1
        return count

    def find_median_2(self, arr: List[List[int]], row: int, col: int)-> int:
        low = arr[0][0]
        high = arr[0][col - 1]
        for i in range(1, row):
            if arr[i][0] < low:
                low = arr[i][0]
            if arr[i][col - 1] > high:
                high = arr[i][col - 1]
        
        median_position = (row * col)//2
        while low <= high:
            mid = low + ((high - low)//2)
            count = self.count_lesser_elements(arr, row, col, mid)
            if count == median_position:
                return mid
            elif count > median_position:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    

if __name__ == "__main__":
    sol = Problem()
    sol.question()