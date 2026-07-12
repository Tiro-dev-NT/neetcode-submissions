from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for w in strs:
            key = ''.join(sorted(w))
            group[key].append(w)
        return list(group.values())