class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            if len(word) not in self.d:
                self.d[len(word)] = [word]
            else:
                self.d[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.d:
            return False

        words = self.d[len(searchWord)]
        for word in words:
            mismatched = 0
            for i in range(len(searchWord)):
                if mismatched > 1:
                    break
                if word[i] != searchWord[i]:
                    mismatched += 1
            if mismatched == 1:
                return True
