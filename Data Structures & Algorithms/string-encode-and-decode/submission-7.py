class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        if not strs:
            return ""

        lengths = [len(s) for s in strs]

        encoded = ""

        for i in range(len(strs)):
            encoded += f"{lengths[i]}#{strs[i]}"

        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        strs = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            strs.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length

        return strs