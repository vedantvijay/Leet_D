class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        result = "".join(chunks)
        ans = []
        pattern = r"[a-z]+(?:-[a-z]+)*"
        
        valid_words = re.findall(pattern, result)
        word_counts = Counter(valid_words)
        for i in queries:
            ans.append(word_counts[i])

        return ans
