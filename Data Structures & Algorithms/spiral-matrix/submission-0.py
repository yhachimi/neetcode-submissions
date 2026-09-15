class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:


        top = 0 
        bottom = len(matrix) - 1 
        left = 0 
        right =  len(matrix[0]) - 1
        res = []

        while top <= bottom  and left <= right:
            

            #left to right 
            for col  in range(left, right +  1):
                res.append(matrix[top][col])

            top += 1 
            #go down

            for row in range(top, bottom + 1,):
                res.append(matrix[row][right])

            right -= 1 

            #right to  left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])


                bottom -= 1

            #go up
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res









