class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mismatch_count = 0
        first_index_diff = 0
        second_index_diff = 0
        for idx, ch in enumerate(s1):
            if ch != s2[idx]:
                mismatch_count += 1

                if mismatch_count > 2:
                    return False
                elif mismatch_count == 1:
                    # store the index of first difference
                    first_index_diff = idx
                else:
                    # store the index of second difference
                    second_index_diff = idx 
            
            

        return (
            s1[first_index_diff] == s2[second_index_diff]
            and s1[second_index_diff] == s2[first_index_diff]
        )