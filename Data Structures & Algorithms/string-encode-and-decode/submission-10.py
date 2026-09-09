class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''

        l = [len(s) for s in strs]
        s = ""

        for i in range(len(strs)):
            word = strs[i]
            length = l[i]
            s += f'{length}#{word}'

        return s


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        i = 0
        words = []

        while i < len(s):
            j = i 

            while s[j] != "#":
                j += 1 

            length = int(s[i : j])
            words.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return words

