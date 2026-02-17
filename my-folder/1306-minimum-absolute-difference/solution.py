class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        min_difference = float('inf')
        result = []
        for i in range(n-1):
            curr_difference = arr[i+1]-arr[i]
            if curr_difference<min_difference:
                min_difference = curr_difference
                result = [[arr[i],arr[i+1]]]
            elif curr_difference == min_difference:
                result.append([arr[i],arr[i+1]])
        return result
            
        
