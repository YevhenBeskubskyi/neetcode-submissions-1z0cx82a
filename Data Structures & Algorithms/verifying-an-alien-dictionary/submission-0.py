class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c:i for i, c in enumerate(order)}

        def compare(word1, word2):
            print(word1, word2)
            m = min(len(word1), len(word2))
            if word1[:m] == word2[:m] and len(word2) < len(word1):
                print('Case 1')
                return False
            for j in range(m):
                if d[word1[j]] < d[word2[j]]:
                    return True
                elif d[word1[j]] == d[word2[j]]:
                    continue
                else:
                    print(f'{word1[j]}:{d[word1[j]]}')
                    print(f'{word2[j]}:{d[word2[j]]}')
                    return False
            return True

        
        return all([compare(words[i-1], words[i]) for i in range(1, len(words))])