class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        
        min_diff = float("inf")
        n = len(arr)    
    
        for i in range(n - 1):
            diff = arr[i+1] - arr[i]
            min_diff = min(min_diff, diff)
        
        result = []


        for i in range(n - 1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i], arr[i+1]])
        
        return result

