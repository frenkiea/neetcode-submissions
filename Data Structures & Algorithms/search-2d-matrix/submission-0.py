class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def checki(arr):
            left = 0
            right = len(arr) - 1
    
            while left <= right:
                mid = left + (right - left) // 2
    
                if arr[mid] == target:
                    return mid
    
                elif target < arr[mid]:
                    right = mid - 1
    
                else:
                    left = mid + 1
            return -1
    
        up = 0
        down = len(matrix) - 1
    
        while up <= down:
            mid = up + (down - up) // 2
    
            if checki(matrix[mid]) != -1:
                return True
    
            elif target < matrix[mid][0]:
                down = mid - 1
    
            else:
                up = mid + 1
    
        return False