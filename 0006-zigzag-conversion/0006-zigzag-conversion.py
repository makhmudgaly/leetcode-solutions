class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        column_offset = 2* (numRows - 1)
        res = []

        if numRows == 1:
            return s

        for row in range(numRows):
            idx = row

            while idx < n:
                res.append(s[idx])

                if row != 0 and row != numRows - 1:
                    in_between = column_offset - 2 * row
                    if idx + in_between < n:
                        res.append(s[idx + in_between])
                
                idx += column_offset



        return "".join(res)