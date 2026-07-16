class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = []
        for i in strs:
            new_str.append(str(len(i)) + "#" + i)
        return "".join(new_str)
    def decode(self, s: str) -> List[str]:
        decode_strs = []
        i = 0
        while i < len(s):
            k = s.find("#", i)
            q = int(s[i:k])
            decode_strs.append(s[k+1:k+1+q])
            i = k+1+q
        return decode_strs


