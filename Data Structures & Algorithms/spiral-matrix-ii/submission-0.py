class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0] * n for _ in range(n)]






        top = 0 
        bottom = n - 1
        left = 0
        right = n - 1
        n = 0

        while top <= bottom  and left <= right:
            #left to right 


            for col  in range(left, right + 1):
                n += 1
                matrix[top][col] = n 
            
            top += 1


            for row  in range(top, bottom + 1):
                n += 1
                matrix[row][right] = n 

            right -= 1

            for col  in range(right, left - 1, -1):
                n += 1
                matrix[bottom][col] = n 

            bottom -= 1

            for row  in range(bottom, top - 1, -1):
                n += 1
                matrix[row][left] = n

            left += 1 

                   
   
        return matrix        