class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res = res + str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # move j to find the delimiter
            while s[j] != '#':
                j += 1
            length = int(s[i:j])      # length before '#'
            i = j + 1                 # move past '#'
            word = s[i:i + length]    # grab the actual string
            res.append(word)
            i += length               # move to the next encoded string
        return res