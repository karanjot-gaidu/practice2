class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for s in strs:
            encode.append(str(len(s)) + "#" + s)
        return "".join(encode)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            j += 1

            result.append(s[j:j+length])
            i = j+length
        return result