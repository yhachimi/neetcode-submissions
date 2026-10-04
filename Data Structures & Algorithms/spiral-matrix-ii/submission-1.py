class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0] * n for i  in range(n)]




        top = 0 

        down = n - 1
        left = 0 
        right = n - 1

        num = 1
        while top <= down and left <= right:
            

            ## go left


            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1


            top += 1
            ## do down 

            for row in range(top, down + 1):
                matrix[row][right] = num 
                num += 1

            right -= 1 

            for col  in range(right, left - 1, -1):
                matrix[down][col] = num
                num += 1


            down -= 1 


            for row in range(down, top - 1, -1):
                matrix[row][left] = num 
                num += 1


            left += 1


        return matrix        