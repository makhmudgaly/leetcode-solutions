class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_dict = defaultdict(list)
        max_value = -1
        for num in nums:
            digit_sum = calculate_digit_sum(num)
            heapq.heappush(digit_sum_dict[digit_sum], num)

            if len(digit_sum_dict[digit_sum]) > 2:
                heapq.heappop(digit_sum_dict[digit_sum])
        
        for numbers in digit_sum_dict.values():
            if len(numbers) == 2:
                max_value = max(max_value, sum(numbers))

        return max_value

def calculate_digit_sum(num):
    curr_sum = 0
    while num != 0:
        curr_sum += num % 10
        num //= 10
    
    return curr_sum