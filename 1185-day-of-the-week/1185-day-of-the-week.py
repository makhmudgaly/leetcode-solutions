class Solution:
    def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        from datetime import datetime
        return days[datetime(y, m, d).weekday()]
        