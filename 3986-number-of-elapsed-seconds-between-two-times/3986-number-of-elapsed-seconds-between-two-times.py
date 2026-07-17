class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        return self.convert_2_sec(endTime) - self.convert_2_sec(startTime)
        
    def convert_2_sec(self, time: str):
        hh, mm, ss = [int(x) for x in time.split(':')]
        return hh * 3600 + (mm * 60) + ss