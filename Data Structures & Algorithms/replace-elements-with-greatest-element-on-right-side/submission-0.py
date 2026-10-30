class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_current_value = -1
        for i in range(len(arr)-1,-1,-1):
            current_value = arr[i]
            arr[i] = max_current_value
            max_current_value = max(max_current_value, current_value)
        return arr
            

                
       
        