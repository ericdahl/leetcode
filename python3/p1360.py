class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        (d1_y, d1_m, d1_d) = (int(v) for v in date1.split("-"))
        (d2_y, d2_m, d2_d) = (int(v) for v in date2.split("-"))
        
        d1 = datetime.datetime(d1_y, d1_m, d1_d)
        d2 = datetime.datetime(d2_y, d2_m, d2_d)

        return abs((d1 - d2).days)
