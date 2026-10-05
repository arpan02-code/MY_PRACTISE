class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = 0
        length = n - 1
        

        for i in range(n):
        
            if i > length - zeros:
                break
            if arr[i] == 0:
            
                if i == length - zeros:
                    arr[length] = 0
                    length -= 1
                    break
                zeros += 1
                
    
        last = length - zeros
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + zeros] = 0
                zeros -= 1
                arr[i + zeros] = 0
            else:
                arr[i + zeros] = arr[i]
