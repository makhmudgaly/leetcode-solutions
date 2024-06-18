class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_profile = [
            (difficulty[i], profit[i]) for i in range(len(difficulty))
        ]

        # Sort both worker and job_profile arrays

        worker.sort()
        job_profile.sort()

        net_profit, max_profit, index = 0, 0, 0
        for ability in worker:
            # While the index has not reached the end and worker can pick a job
            # with greater difficulty move ahead.

            while index < len(difficulty) and ability >= job_profile[index][0]:
                max_profit = max(max_profit, job_profile[index][1])
                index += 1
            net_profit += max_profit
        return net_profit