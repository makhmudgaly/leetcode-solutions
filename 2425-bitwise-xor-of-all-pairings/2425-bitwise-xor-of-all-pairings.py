class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        def get_xor(arr):
            ans = 0
            for x in arr:
                ans ^= x
            
            return ans
        
        firstEven = len(nums1) % 2 == 0
        secondEven = len(nums2) % 2 == 0
       
        
        if firstEven and secondEven:
            return 0
        
        
        if not firstEven and not secondEven:
            return get_xor(nums1 + nums2)
                
        if not firstEven:
            return get_xor(nums2)
        
        return get_xor(nums1)
    
        