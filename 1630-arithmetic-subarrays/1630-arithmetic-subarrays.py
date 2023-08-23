class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for (left, right) in zip(l,r):
            sub_arr = sorted(nums[left:right+1])
            flag = True
            prev = sub_arr[1] - sub_arr[0]
            
            for i in range(0, len(sub_arr)-1, 1):
                if prev != sub_arr[i+1] - sub_arr[i]:
                    flag = False
                    break
                
                prev = sub_arr[i+1] - sub_arr[i]
            ans.append(flag)
            
        return ans